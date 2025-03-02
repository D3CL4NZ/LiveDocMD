# LiveDocMD

LiveDocMD is an innovative website that uses artificial intelligence to help you better understand your health. Whether you're experiencing symptoms or just looking for general health advice, with the help of Gemini AI it analyzes your input and provides you with possible health diagnoses and recommendations. Our goal is to help you make informed decisions about your well-being and take proactive steps toward improving your health.

## Project Structure

```
livedocmd
├── src
│   ├── app.py          # Main entry point of the application
│   ├── templates
│   │   └── index.html  # HTML structure for the web page
│   └── static
│       ├── styles.css  # CSS styles for the web page
│       ├── favicon.ico # The favicon
│       └── logo.png    # Our logo
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to have Python installed. You can install the required dependencies using the following command inside your `venv`:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:
   ```zsh
   cd livedocmd
   ```

2. Create a `.env` file for your API key:
   ```zsh
   echo "GOOGLE_GEMINI_API_KEY='[REDACTED]'" > .env
   ```

2. Run the application:
   ```zsh
   python3 src/app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the web application.

## Usage

Once the web server is running, you will see a text box in the center of the screen. Enter your AI prompt and click the submit button to send the prompt to the server for processing.
