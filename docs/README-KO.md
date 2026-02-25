<div align="center">

# How Many Cals (AI )

**Google Gemini 2.5 FlashAI LINE .** <br>
*[fastapi-line-gemini](https://github.com/welltilln/fastapi-line-gemini) .*

<p align="center">
    <a href="../README.md">English</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-TH.md">ภาษาไทย</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-ZH.md">简体中文</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-JA.md">日本語</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-KO.md">한국어</a>
</p>

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a67d?logo=fastapi)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?logo=google)](https://ai.google.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-Persistent_Storage-003B57?logo=sqlite)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<br/>

## **How Many Cals** LINE . GoogleGemini Vision .

, **SQLite **. , AI .

---

## * **:** (: ).
* **DB:** SQLite. .
* **:** . 0.
* **:** AI, . .
* **(Zero-config) :** `run.sh` / `run.bat` , , Ngrok .

---

## ```mermaid
sequenceDiagram
    participant User as LINE participant LINE as LINE participant App as FastAPI participant DB as SQLite DB
    participant Gemini as Google Gemini API

    User->>LINE: /LINE->>App: Webhook POST rect rgb(200, 220, 240)
        Note right of App: DB App->>DB: / end

    App->>Gemini: + + Gemini-->>App: rect rgb(200, 220, 240)
        App->>DB: end

    App-->>LINE: Reply API POST LINE-->>User: ```

---

## (Quick Setup)

### API .
1. **[LINE Messaging API](https://developers.line.biz/console/):** `Channel Secret` `Channel Access Token` .
2. **[Google Gemini API Key](https://aistudio.google.com/):** Google AI StudioAPI .
3. **[Ngrok Auth Token](https://dashboard.ngrok.com/):** LINE .

### 1: ```bash
git clone https://github.com/welltilln/howmanycals.git
cd howmanycals
```
`.env.example` `.env`. API :
```env
LINE_CHANNEL_SECRET=_secret_LINE_CHANNEL_ACCESS_TOKEN=_token_GEMINI_API_KEY=_gemini_key_NGROK_AUTHTOKEN=_ngrok_token_```

### 2: 1-Click **MacOS / Linux** :
```bash
./run.sh
```
**Windows** :
```cmd
run.bat
```
*(, FastAPI , `users.db`Ngrok .)*

### 3: LINE Ngrok URL (: `https://xxxx.ngrok.app/callback`). LINE Developers Console **Webhook URL** Verify !

---

## (Docker )

Ngrok VPS()24, Docker .

1. [Docker](https://docs.docker.com/get-docker/) [Docker Compose](https://docs.docker.com/compose/) .
2. :
```bash
docker-compose up -d --build
```
*: `users.db`(Volume) , .*

---

## AI (Language & Persona Customization)

. .

1. `app/gemini.py` .
2. `system_prompt` .
3. , .

**():**
```python
system_prompt = """
AI . .
.

:
: []
: [] kcal
: [] kcal
"""
```

**():**
```python
system_prompt = """
. .
. 500kcal50.

:
: [] kcal
: []
: [] kcal
"""
```

### AI (Future-Proofing)
Gemini (: Gemini 3.0)! `app/gemini.py` `model_name` .
```python
model = genai.GenerativeModel(
  model_name="gemini-3.0-pro", # <-- ...
)
```

---

## (FAQ)

**Q: (12)0?**
**A:** CPU "()" . , . .

**Q: .**
**A:** (). . Google API .

**Q: ()?**
**A:** ! `system_prompt` "".

---

## (License)

MIT License . [LICENSE](../LICENSE) .
