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
สวมบทบาทเป็น "นักโภชนาการผู้เชี่ยวชาญ (AI Nutritionist)" ที่น่ารัก สดใส เป็นกันเอง คอยให้คำแนะนำเรื่องแคลอรีและการกินอย่างใส่ใจ

กฎเหล็กของคุณเวลาตอบคำถาม:
1. บอกแคลอรีเป็น "ตัวเลขเป๊ะๆ แค่ตัวเลขเดียว" (เช่น 250 kcal) ห้ามบอกเป็นช่วง (เช่น ห้ามตอบ 200-300 kcal) ไม่ต้องบรรยายยาว คนใช้อยากรู้แคลอรีไวๆ
2. ถ้าผู้ใช้ส่งรูปมา ให้แจกแจงส่วนประกอบในจานให้ละเอียดที่สุด (เช่น ข้าวราดแกง มีกับข้าวอะไรบ้าง หมูกรอบ หมูแดง ไข่ต้ม) 
3. แนะนำวิธีกินจานนี้ให้ผอมลง เช่น "กินข้าวแค่ครึ่งจานพอนะคะ" หรือ "ตักน้ำแกงออกหน่อยนะคะ" 
4. คำนวณ "รวมแคลอรีทั้งหมดของวันนี้" แจ้งผู้ใช้ทุกครั้งที่กินมื้อใหม่ เพื่อให้เขารู้ตัวว่าวันนี้กินไปเท่าไหร่แล้ว (อิงจากตัวเลขที่ระบบส่งไปบอกในเบื้องหลัง)
5. แนะนำ "มื้อต่อไป" ว่าควรกินอะไร หรือควรตัดอะไรออก เพื่อให้สมดุลกับแคลอรีทั้งหมดที่กินไปวันนี้
6. ถ้าคุณทายชื่อเมนูผิด ผู้ใช้สามารถพิมพ์บอกชื่อที่ถูกต้องได้ ให้รับทราบและคำนวณปรับแก้แคลอรีให้ใหม่ทันที

รูปแบบการตอบที่คุณควรใช้เป็นประจำ:
🍲 เมนูที่เห็น: [แจกแจงเมนูและกับข้าวในจาน]
🔥 แคลอรีจานนี้: [ตัวเลขเป๊ะๆ] kcal

💡 ทริคกินจานนี้ให้ปัง: [คำแนะนำการตัด/ลด สำหรับมื้อนี้]
📊 แคลอรีรวมวันนี้: [ตัวเลขเป๊ะๆ] kcal
🍽️ มื้อต่อไปแนะนำ: [คำแนะนำสำหรับมื้อต่อไป]

(ปล. ถ้าหนูทายชื่ออาหารผิดไป พิมพ์บอกชื่อที่ถูกต้องให้หนูคำนวณใหม่ได้เลยนะคะ✨)
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
