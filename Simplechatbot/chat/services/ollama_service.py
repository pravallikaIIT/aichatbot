import requests
import sqlite3
from database import DB_NAME

def save_message(user_id, sender, message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (user_id, sender, message) VALUES (?, ?, ?)",
        (user_id, sender, message)
    )
    conn.commit()
    conn.close()

def get_conversation_history(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sender, message FROM messages WHERE user_id = ? ORDER BY id",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    conversation = [f"{sender}: {message}" for sender, message in rows]
    return "\n".join(conversation)

def generate_response(user_id, user_message):
    # Save user message
    save_message(user_id, "User", user_message)

    # Get full conversation for context
    prompt = get_conversation_history(user_id)

    # Call Ollama local LLM
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        ai_reply = response.json().get("response", "Sorry, I couldn't generate a response.")
    except Exception as e:
        ai_reply = "AI server is not available."

    # Save AI reply
    save_message(user_id, "AI", ai_reply)
    return ai_reply