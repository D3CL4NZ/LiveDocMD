from flask import Flask, render_template, request, Response
import os
from google import genai

from dotenv import load_dotenv

load_dotenv()

# Set up your Google Gemini AI API key
client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/stream_response', methods=['POST'])
def stream_response():
    user_input = request.form['prompt']

    def generate():
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash", contents=user_input
        )
        for chunk in response:
            yield chunk.text

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
