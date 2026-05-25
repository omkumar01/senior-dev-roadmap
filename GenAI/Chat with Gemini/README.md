# Gemini Chat App

A simple chat application using Google's Gemini AI and Streamlit.

## Setup Instructions

### 1. Get a Gemini API Key
- Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
- Create a free API key

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` File
Create a `.env` file in the same directory and add your API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Running with Docker

### Option 1: Using Docker Compose (Recommended)
```bash
# Create .env file with your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Build and run the container
docker-compose up --build
```

### Option 2: Using Docker CLI
```bash
# Build the image
docker build -t gemini-chat .

# Run the container
docker run -p 8501:8501 -e GEMINI_API_KEY=your_api_key_here gemini-chat
```

The app will be available at `http://localhost:8501`

## Features
- 💬 Real-time chat with Gemini AI
- 📝 Chat history within the session
- 🎨 Clean and simple Streamlit interface
- 🔒 API key stored securely in .env file

## Notes
- This app uses the `gemini-pro` model
- Chat history resets when you refresh the page
- Make sure your `.env` file is in `.gitignore` to keep your API key private
