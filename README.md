# My Python Web Server

This project sets up a simple web server using Flask that allows users to input prompts for an AI model. The user interface features a text box centered on the screen for easy input.

## Project Structure

```
my-python-web-server
├── src
│   ├── app.py          # Main entry point of the web server
│   ├── templates
│   │   └── index.html  # HTML structure for the web page
│   └── static
│       └── styles.css  # CSS styles for the web page
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to have Python installed. You can install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Running the Web Server

1. Navigate to the project directory:
   ```
   cd my-python-web-server
   ```

2. Run the application:
   ```
   python src/app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the web application.

## Usage

Once the web server is running, you will see a text box in the center of the screen. Enter your AI prompt and click the submit button to send the prompt to the server for processing.