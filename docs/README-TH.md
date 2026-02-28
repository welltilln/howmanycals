<div align="center">

# How Many Cals (AI Nutritionist)

** LINE  AI  Production  Google Gemini 2.5 Flash** <br>
* [fastapi-line-gemini](https://github.com/welltilln/fastapi-line-gemini)*

<p align="center">
    <a href="../README.md">English</a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-TH.md"></a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-ZH.md"></a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-JA.md"></a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-KO.md"></a>
</p>

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a67d?logo=fastapi)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?logo=google)](https://ai.google.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-Persistent_Storage-003B57?logo=sqlite)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<br/>

##  (Overview)

**How Many Cals**  LINE  (Vision)  Google Gemini    

  ** (Persistent SQLite Memory)**    AI 

---

##  (Key Features)

* **:**  ( ) 
* ** SQLite :**   
* **:**   
* ** ""  AI:**  AI   
* ** Zero-Config:**  `run.sh` / `run.bat`   Environment,  Dependencies  Ngrok Tunnel 

---

##  (Architecture)

```mermaid
sequenceDiagram
    participant User as LINE User
    participant LINE as LINE Platform
    participant App as FastAPI Server
    participant DB as SQLite DB
    participant Gemini as Google Gemini API

    User->>LINE: ส่งรูปภาพอาหาร/ข้อความ
    LINE->>App: ส่ง Webhook POST Request
    Note right of App: เลเยอร์ฐานข้อมูล (Database)
    App->>DB: ดึงข้อมูล/รีเซ็ตแคลอรี่รายวัน
    App->>Gemini: ส่งรูปภาพ + ยอดแคลอรี่ปัจจุบัน + System Prompt
    Gemini-->>App: แยกส่วนประกอบอาหารและแคลอรี่รวม
    App->>DB: อัปเดตแคลอรี่รวมใหม่ลงใน DB
    App-->>LINE: ส่ง POST API เพื่อ Reply Message
    LINE-->>User: บอทตอบกลับพร้อมสรุปแคลอรี่
```

---

##  (Quick Start Setup)

###  (Prerequisites)
1. **[LINE Messaging API](https://developers.line.biz/console/):**  `Channel Secret`  `Channel Access Token`  LINE
2. **[Google Gemini API Key](https://aistudio.google.com/):**  API Key  Google AI Studio
3. **[Ngrok Auth Token](https://dashboard.ngrok.com/):**  Webhook  LINE 

###  1: 
```bash
git clone https://github.com/welltilln/howmanycals.git
cd howmanycals
```
 `.env.example`  `.env`  API Key :
```env
LINE_CHANNEL_SECRET=your_secret_here
LINE_CHANNEL_ACCESS_TOKEN=your_token_here
GEMINI_API_KEY=your_gemini_key_here
NGROK_AUTHTOKEN=your_ngrok_token_here
```

###  2: 
 **MacOS / Linux**:
```bash
./run.sh
```
 **Windows**:
```cmd
run.bat
```
*(   FastAPI   `users.db`   Ngrok Tunnel )*

###  3:  Webhook  LINE 
 Ngrok URL  Terminal ( `https://xxxx.ngrok.app/callback`)  **Webhook URL**  LINE Developers Console  Verify !

---

##  Production (Docker)

 VPS  ( 24   Ngrok)  Docker  Enterprise :

1.  [Docker](https://docs.docker.com/get-docker/)  [Docker Compose](https://docs.docker.com/compose/) 
2.  Background (Detached Data):
```bash
docker-compose up -d --build
```
*:  `users.db`  Mount  Volume  !*

---

##  AI (Language & Persona Customization)

     (Reprogram)  :

1.  `app/gemini.py`
2.  `system_prompt`
3.  (`"""`)  

** ():**
```python
system_prompt = """
 AI  
 

 ():
 : []
: [ ] kcal
: [] kcal
"""
```

** ():**
```python
system_prompt = """
 "" 
 
   500 kcal   50 

 ():
: [ ] kcal
: []
: [] kcal
"""
```

###  AI (Future-Proofing)
 Google  ( Gemini 3.0) !  `app/gemini.py`  `model_name` :
```python
model = genai.GenerativeModel(
  model_name="gemini-3.0-pro", # <-- 
  ...
)
```

---

##  (FAQ)

**Q: ?**
**A:**  " (On-Demand Logic)"   ( Job )  Timezone  

**Q:  Error  Log ?**
**A:**  Local  Log  Terminal    Timeout  Google Gemini API

**Q:  AI ?**
**A:** !  `system_prompt`    

---

##  (Built With)
- **[FastAPI](https://fastapi.tiangolo.com/)** -  Python 
- **[Google Generative AI](https://ai.google.dev/)** -  Gemini 1.5/2.5 Flash Vision Models
- **[LINE Messaging API SDK](https://github.com/line/line-bot-sdk-python)** -  Webhooks  LINE
- **SQLite** -   Database Server  

##  (License)

 MIT License -  [LICENSE](../LICENSE) 
