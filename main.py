import os
from google import genai

from dotenv import load_dotenv

load_dotenv()

# Set up your Google Gemini AI API key
client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

def get_gemini_response(prompt):
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash", contents=prompt
    )
    return response

def chatbot():
    print("Hello! I am a chatbot powered by Google Gemini AI. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = get_gemini_response(user_input)
        print(f"Chatbot: ", end="")
        for chunk in response:
            print(chunk.text, end="")

if __name__ == "__main__":
    chatbot()
