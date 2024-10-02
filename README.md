# howmanycals
AI for estimating calories using Line Developer and Gemini.

how to use:

create venv by using requirements.txt

then

put your token in .env file

then run

-> ngrok 'static domain' (you can get it by go to [ngrok website)](https://dashboard.ngrok.com/get-started/setup/)

*Make sure you set the port correctly; if you use the wrong port number, the static domain may not work. You can modify the static domain's final port number to the one you're using.*

then run

-> uvicorn main:app  --reload
