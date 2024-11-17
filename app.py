from flask import Flask, render_template, request
import pyttsx3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form.get('text')
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    return "Speech Synthesis Done!"

if __name__ == '__main__':
    # Utilisez le port défini par Render ou par défaut 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
