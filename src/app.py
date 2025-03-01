from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    if request.method == 'POST':
        user_input = request.form['prompt']
        # Here you would typically process the user_input with your AI model
    return render_template('index.html', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)