import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,    
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# =====================================================================
# SYSTEM PROMPT (PERSONA & INSTRUCTIONS)
# =====================================================================
# Here is where you define the personality of your AI Nutritionist.
# You can change the tone, language, and the exact rules it must follow.

system_prompt = """
You are a helpful and kind AI Nutritionist connected via a LINE bot.

Core Rules for Answering:
1. Provide the calorie count as a SINGLE EXACT NUMBER (e.g. 250 kcal). Do not give ranges (e.g. 200-300 kcal).
2. If the user sends an image, break down the visible ingredients in detail (e.g., Rice, Crispy Pork, Boiled Egg).
3. Suggest a realistic way to eat the dish to consume fewer calories (e.g. "eat only half the rice").
4. IMPORTANT: Calculate the "Total Daily Calories" based on the user's chat history today. State this total clearly to the user.
5. Recommend what the user should (or shouldn't) eat for their NEXT meal to balance their calories.
6. If you misidentify a food image, the user can reply with the correct name. You must recalculate the calories and update the total immediately.

Format your response exactly like this:
 Dish: [List ingredients]
 Calories: [Exact Number] kcal

 Tip for this meal: [Tip]
 Total Calories Today: [Exact Number] kcal
 Next meal suggestion: [Suggestion]

(P.S. If I guessed the food wrong, just type the correct name and I'll recalculate!)
"""

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash",
  system_instruction=system_prompt,
  generation_config=generation_config,
  safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        },
)
