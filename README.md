# aichatbot
AI Chatbot with OLLAMA Integration

# Navigate to project folder
cd C:\Users\DELL\PycharmProjects\Simplechatbot\chat

# Create Python virtual environment
python -m venv venv

# Activate virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install Python dependencies
python -m pip install flask flask-cors requests

# Initialize SQLite database (optional)
python
>>> import sqlite3
>>> conn = sqlite3.connect("chat.db")
>>> c = conn.cursor()
>>> c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT, sender TEXT, message TEXT)''')
>>> conn.commit()
>>> conn.close()
>>> exit()

# Run Flask backend
python server.py

# Start Ollama AI server
ollama serve

# Navigate to React frontend folder
cd ai-frontend

# Install React and dependencies
npm install
npm install react react-dom
npm install react-typing-animation

# Start React frontend
npm start

# Optional: Test backend API via curl
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"message": "Hi", "user_id": "user1"}'

# Optional: Deactivate Python virtual environment
deactivate