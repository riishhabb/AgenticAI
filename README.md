# 🤖 AgenticAI – Compassionate Mental Health Support Chatbot

AgenticAI is a lightweight, web-based AI companion built using **Flask** and powered by **Claude 3 Haiku** from Anthropic. Designed to provide **empathetic**, **non-judgmental** support for mental wellness, AgenticAI is your go-to chatbot for encouragement and kind conversations.

---

## 🌟 Features

- Built with Flask and HTML/CSS for simplicity and speed
- Uses Claude 3 Haiku LLM for real-time emotional support
- System prompt crafted for compassionate interactions
- API integration with Anthropic’s SDK
- Cross-Origin support for flexible frontend-backend setup

---

## 📁 Project Structure

```
AgenticAI/
├── app.py              # Flask backend with /chat API
├── index.html          # Frontend UI for the chatbot
├── .gitignore
├── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/riishhabb/AgenticAI.git
cd AgenticAI
```

### 2. Set Up Environment

Create a `.env` file in the root directory:

```
CLAUDE_API_KEY=your_claude_api_key_here
```

> You can get an API key from [Anthropic Console](https://console.anthropic.com/).

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Or install individually:

```bash
pip install flask flask-cors anthropic python-dotenv
```

### 4. Run the App

```bash
python app.py
```

The app will be live at: `http://127.0.0.1:5000/`

---

## 📡 API Endpoint

### POST `/chat`

**Request:**
```json
{
  "message": "I'm feeling down today."
}
```

**Response:**
```json
{
  "response": "I'm here for you. Want to talk about what's been bothering you?"
}
```

---

## 🛡️ Security Notes

- Never hardcode your API key in production.
- Add authentication, rate limiting, and logging for better robustness.

---

## 💡 Future Ideas

- User chat history and login
- Emotion detection from user messages
- Custom avatars and voice integration
- Mobile-friendly UI
