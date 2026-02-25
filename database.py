import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")

def init_db():
    """Initialize the SQLite database and create the users table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            last_active_date TEXT,
            daily_calories INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def get_user(user_id: str):
    """Retrieve user data. If the user doesn't exist, create a new record."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT last_active_date, daily_calories FROM users WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    if row is None:
        # New user
        cursor.execute('INSERT INTO users (user_id, last_active_date, daily_calories) VALUES (?, ?, ?)',
                       (user_id, current_date, 0))
        conn.commit()
        last_active_date = current_date
        daily_calories = 0
    else:
        last_active_date = row[0]
        daily_calories = row[1]
        
    conn.close()
    return {"last_active_date": last_active_date, "daily_calories": daily_calories}

def reset_daily_calories_if_new_day(user_id: str) -> dict:
    """Check if it's a new day. If so, reset calories to 0. Return updated user data."""
    user_data = get_user(user_id)
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    if user_data["last_active_date"] != current_date:
        # It's a new day, reset calories
        user_data["daily_calories"] = 0
        user_data["last_active_date"] = current_date
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users SET last_active_date = ?, daily_calories = ? WHERE user_id = ?
        ''', (current_date, 0, user_id))
        conn.commit()
        conn.close()
        
    return user_data

def update_user_calories(user_id: str, added_calories: int):
    """Add new calories to the user's daily total and update the last active date."""
    # Ensure any daily reset happens first before adding
    user_data = reset_daily_calories_if_new_day(user_id)
    
    new_total = user_data["daily_calories"] + added_calories
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users SET last_active_date = ?, daily_calories = ? WHERE user_id = ?
    ''', (current_date, new_total, user_id))
    conn.commit()
    conn.close()
    
    return new_total

# Initialize the db when module is imported
init_db()
