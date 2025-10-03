import os
import base64
import json
from flask import Flask, render_template, request
from flask_cors import CORS
from worker import speech_to_text, text_to_speech, openai_process_message

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    audio_binary = request.data  # user's speech
    text = speech_to_text(audio_binary)

    # Return the response to user in JSON format
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage']

    # Get selected voice
    voice = request.json['voice']

    # Process user's message and get a response back
    openai_response_text = openai_process_message(user_message)

    # Remove empty lines
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])

    # Convert reponse to speech
    openai_response_speech = text_to_speech(openai_response_text, voice)

    # Convert to base64 string, so it can be sent back in the JSON response
    openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

    # Send a JSON response containing their message's response both in text and speech formats
    response = app.response_class(
        response=json.dumps({"openaiResponseText": openai_response_text, "openaiResponseSpeech": openai_response_speech}),
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
