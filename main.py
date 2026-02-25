import os
import sys
from dotenv import load_dotenv
load_dotenv()
from fastapi import Request, FastAPI, HTTPException
from gemini import model
from PIL import Image
import io
import database  # Import the new SQLite database manager

from linebot.v3.webhook import WebhookParser
from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    ReplyMessageRequest,
    TextMessage,
    ShowLoadingAnimationRequest,
    AsyncMessagingApiBlob
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    ImageMessageContent
)


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

configuration = Configuration(
    access_token=channel_access_token
)

app = FastAPI()
async_api_client = AsyncApiClient(configuration)
line_bot_api = AsyncMessagingApi(async_api_client)
parser = WebhookParser(channel_secret)

user_sessions = {}

@app.post("/callback")
async def handle_callback(request: Request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
       
        # Start or get user session
        user_id = event.source.user_id
        if user_id not in user_sessions:
            user_sessions[user_id] = model.start_chat()
        
        chat = user_sessions[user_id]

        # Show loading animation (>5)
        await line_bot_api.show_loading_animation(
            ShowLoadingAnimationRequest(chatId=user_id, loadingSeconds=30)
        )

        user_db = database.get_user(user_id)
        current_total = user_db["daily_calories"]

        if isinstance(event.message, ImageMessageContent):
            image_binary = await AsyncMessagingApiBlob(AsyncApiClient(configuration)).get_message_content(event.message.id)
            image_buffer = io.BytesIO(image_binary)
            image = Image.open(image_buffer)
            
            # Send image to the memory-aware chat object, explicitly telling it the current SQL total
            prompt_context = f"The user has consumed {current_total} kcal so far today. Calculate the calories of this image, and state the NEW Total Calories Today."
            response = chat.send_message([prompt_context, image])
            
            # Extract the actual number from the response via a follow-up hidden prompt (or just rely on the AI text)
            # To keep it simple, we ask Gemini to give us the raw number in a hidden turn, or we can just parse it.
            # For a boilerplate, we'll let Gemini generate the text for the user, and ask it for the exact calorie count of the dish to save to DB.
            raw_cals_response = chat.send_message("Please reply ONLY with the integer of the calories in that last image. E.g., '250' or '0' if it wasn't food. No words.")
            try:
                added_cals = int(raw_cals_response.text.strip())
                database.update_user_calories(user_id, added_cals)
            except ValueError:
                print(f"Failed to parse calories from Gemini: {raw_cals_response.text}")
            
            await line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=response.text)]
                )
            )

        elif isinstance(event.message, TextMessageContent):
            user_text = event.message.text
            
            # Provide context for text conversations as well
            prompt_context = f"The user has consumed {current_total} kcal so far today. Reply to their message: '{user_text}'. If they corrected your previous guess, act on it."
            
            response = chat.send_message(prompt_context)
            
            # If the user is just talking, we don't necessarily update calories, UNLESS they corrected a meal. 
            # We can ask Gemini to tell us the 'adjustment' needed.
            raw_adj_response = chat.send_message("Calculate the adjustment in calories based on this conversation. For example, if you over-guessed by 100, reply '-100'. If it's just a general chat, reply '0'. Reply ONLY with the integer.")
            try:
                adjustment = int(raw_adj_response.text.strip())
                if adjustment != 0:
                     database.update_user_calories(user_id, adjustment)
            except ValueError:
                print(f"Failed to parse adjustment from Gemini: {raw_adj_response.text}")
            
            await line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=response.text)]
                )
            )

    return 'OK'
