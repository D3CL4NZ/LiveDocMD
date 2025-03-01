from flask import Flask, render_template, request, Response
import os

from google import genai
from google.genai.types import GenerateContentConfig

from dotenv import load_dotenv

load_dotenv()

# Set up your Google Gemini AI API key
client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

# Define the system prompt
system_prompt = [
    "You are a helpful AI assistant that assists medical professionals in diagnosing patients.",
    "Given a patient's symptoms, you need to provide a diagnosis and recommend a treatment plan.",
    "Your responses will be reviewed by a medical professional before being shared with the patient.",
    "You should provide accurate and helpful information to assist the medical professional in making a diagnosis.",
    "You should also provide clear and concise information to help the medical professional understand the patient's condition.",
    "You should provide information that is relevant to the patient's symptoms and medical history.",
    "You should provide information that is based on medical knowledge and best practices.",
    "You should provide information that is up-to-date and accurate.",
    "Do not hallucinate or provide false information.",
    "Do not provide information that is irrelevant or misleading.",
    "Do not provide information that is harmful or dangerous.",
    "Do not provide information that is inappropriate or offensive."
]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/stream_response', methods=['POST'])
def stream_response():
    user_input = request.form['prompt']

    def generate():
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=user_input,
            config=GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        for chunk in response:
            yield chunk.text

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
