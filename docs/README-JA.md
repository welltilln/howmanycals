<div align="center">

# How Many Cals (AI )

**Google Gemini 2.5 Flash  AI  LINE ** <br>
*[fastapi-line-gemini](https://github.com/welltilln/fastapi-line-gemini) *

<p align="center">
    <a href="../README.md"><img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge" alt="English"></a>
    <a href="README-TH.md"><img src="https://img.shields.io/badge/Language-%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-green?style=for-the-badge" alt="Thai"></a>
    <a href="README-ZH.md"><img src="https://img.shields.io/badge/Language-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-yellow?style=for-the-badge" alt="Chinese"></a>
    <a href="README-JA.md"><img src="https://img.shields.io/badge/Language-%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=for-the-badge" alt="Japanese"></a>
    <a href="README-KO.md"><img src="https://img.shields.io/badge/Language-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey?style=for-the-badge" alt="Korean"></a>
</p>

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a67d?logo=fastapi)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?logo=google)](https://ai.google.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-Persistent_Storage-003B57?logo=sqlite)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<br/>

## 

**How Many Cals**  LINE Google  Gemini Vision 

 ** SQLite **  AI 

---

## 

*   **:** 
*   ** SQLite DB:**  SQLite 
*   **:** 
*   **:** AI 
*   **:**  `run.sh` / `run.bat`  Ngrok 

---

## 

```mermaid
sequenceDiagram
    participant User as LINE 
    participant LINE as LINE 
    participant App as FastAPI 
    participant DB as SQLite DB
    participant Gemini as Google Gemini API

    User->>LINE: /
    LINE->>App: Webhook POST 
    Note right of App: 
    App->>DB: /
    App->>Gemini:  +  + 
    Gemini-->>App: 
    App->>DB: 
    App-->>LINE:  POST
    LINE-->>User: 
```

---

## 

### 

1.  **[LINE Messaging API](https://developers.line.biz/console/):** `Channel Secret`  `Channel Access Token`
2.  **[Google Gemini API Key](https://aistudio.google.com/):** Google AI Studio  API 
3.  **[Ngrok Auth Token](https://dashboard.ngrok.com/):**  LINE 

###  1: 
```bash
git clone https://github.com/welltilln/howmanycals.git
cd howmanycals
```
`.env.example`  `.env` API 
```env
LINE_CHANNEL_SECRET=your_secret_here
LINE_CHANNEL_ACCESS_TOKEN=your_token_here
GEMINI_API_KEY=your_gemini_key_here
NGROK_AUTHTOKEN=your_ngrok_token_here
```

###  2:  ()
**MacOS / Linux** :
```bash
./run.sh
```
**Windows** :
```cmd
run.bat
```
*(FastAPI `users.db` Ngrok )*

###  3: LINE 
 Ngrok URL: `https://xxxx.ngrok.app/callback`LINE Developers Console  **Webhook URL** Verify

---

##  (Docker)

Ngrok  VPS  24  Docker 

1.   [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/) 
2.  
```bash
docker-compose up -d --build
```
*: `users.db` *

---

## AI 



1.  `app/gemini.py` 
2.  `system_prompt` 
3.  

**:**
```python
system_prompt = """

 500  50 
:
: []
: []
: []
"""
```

---

## FAQ

**Q: **
**A:** 

**Q: **
**A:** Gemini API 

## 

 MIT  [LICENSE](../LICENSE) 