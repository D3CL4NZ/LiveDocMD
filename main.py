import os
import openai

from dotenv import load_dotenv

load_dotenv()

# Set up your Google Gemini AI API key
openai.api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

def get_gemini_response(prompt):
    response = openai.Completion.create(
        engine="gemini",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def chatbot():
    print("Hello! I am a chatbot powered by Google Gemini AI. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = get_gemini_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()