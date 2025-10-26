from openai import OpenAI
import requests

openai_client = OpenAI()


def speech_to_text(audio_binary):
    base_url = 'https://sn-watson-tts.labs.skills.network'
    api_url = base_url + '/speech-to-text/api/v1/recognize'

    params = {
        'model': 'en-US_Multimedia',
    }

    # Send a HTTP Post request
    response = requests.post(api_url, params=params, data=audio_binary).json()

    # Parse the response to get our transcribed text
    text = 'null'
    while bool(response.get('results')):
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        return text


def text_to_speech(text, voice=""):
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    # Adding voice parameter in api_url if the user has selected a preferred voice
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    json_data = {
        'text': text,
    }

    # Send a HTTP Post reqeust to Watson Text-to-Speech Service
    response = requests.post(api_url, headers=headers, json=json_data)
    return response.content


def openai_process_message(user_message):
    prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."

    # Call OpenAI API to process prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=4000
    )

    # Get response message for prompt from OpenAI response
    response_text = openai_response.choices[0].message.content
    return response_text
