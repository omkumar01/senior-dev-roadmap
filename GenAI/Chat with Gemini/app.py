import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the API key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("GEMINI_API_KEY not found. Please set it in your .env file")
    st.stop()

# App title and description
st.set_page_config(page_title="Chat with an AI", layout="centered")
st.title("Chat App")
st.write("Chat with an AI")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get response from Gemini
    try:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            # Call Gemini API
            model = genai.GenerativeModel("gemini-3-flash-preview")
            response = model.generate_content(user_input)
            
            assistant_response = response.text
            message_placeholder.write(assistant_response)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
