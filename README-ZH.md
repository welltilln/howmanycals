<div align="center">

# How Many Cals (AI )

**Google Gemini 2.5 Flash AI LINE ** <br>
*[fastapi-line-gemini](https://github.com/welltilln/fastapi-line-gemini) *

<p align="center">
    <a href="README.md">English</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-TH.md">ภาษาไทย</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-ZH.md"></a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-JA.md"></a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-KO.md"></a>
</p>

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a67d?logo=fastapi)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?logo=google)](https://ai.google.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-Persistent_Storage-003B57?logo=sqlite)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<br/>

## **How Many Cals** LINE Google Gemini Vision “”**SQLite **AI ---

## * **** * **** SQLite * **** * **** AI * **** `run.sh` / `run.bat` Ngrok ---

## ```mermaid
sequenceDiagram
    participant User as LINE participant LINE as LINE participant App as FastAPI participant DB as SQLite participant Gemini as Google Gemini API

    User->>LINE: / LINE->>App: Webhook POST rect rgb(200, 220, 240)
        Note right of App: App->>DB: / end

    App->>Gemini: + + Gemini-->>App: rect rgb(200, 220, 240)
        App->>DB: end

    App-->>LINE: Reply Message
    LINE-->>User: ```

---

## ### API 1. **[LINE Messaging API](https://developers.line.biz/console/):** `Channel Secret` `Channel Access Token`2. **[Google Gemini API Key](https://aistudio.google.com/):** Google AI Studio 3. **[Ngrok Auth Token](https://dashboard.ngrok.com/):** 8000 LINE HTTPS ### ```bash
git clone https://github.com/welltilln/howmanycals.git
cd howmanycals
```
`.env.example` `.env`API ```env
LINE_CHANNEL_SECRET=_secret
LINE_CHANNEL_ACCESS_TOKEN=_token
GEMINI_API_KEY=_gemini_key
NGROK_AUTHTOKEN=_ngrok_token
```

### **MacOS / Linux** ```bash
./run.sh
```
**Windows** ```cmd
run.bat
```
*(FastAPI `users.db` Ngrok )*

### LINE Ngrok URL`https://xxxx.ngrok.app/callback`LINE **Webhook URL** Verify ---

## (Docker)

Ngrok (VPS) Docker 1. [Docker](https://docs.docker.com/get-docker/) [Docker Compose](https://docs.docker.com/compose/)2. ```bash
docker-compose up -d --build
```
*: `users.db` (Volume) *

---

## AI (Language & Persona Customization)

1. `app/gemini.py`2. `system_prompt` 3. ****
```python
system_prompt = """
AI []
[] [] """
```

**“”**
```python
system_prompt = """
500 50 [] []
[] """
```

### (Future-Proofing)
Gemini 3.0`app/gemini.py``model_name` ```python
model = genai.GenerativeModel(
  model_name="gemini-3.0-pro", # <-- ...
)
```

---

## (FAQ)

**Q: 12 **
**A:** “On-Demand”**Q: **
**A:** LINE “”Gemini **Q: **
**A:** `system_prompt`“/”---

## MIT - [LICENSE](LICENSE) 