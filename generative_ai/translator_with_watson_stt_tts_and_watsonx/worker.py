import requests

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods

# Placeholder for credentials to use code outside Skills Network
# API_KEY = "Your WatsonX API"
PROJECT_ID = "skills-network"

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
    # "apikey": API_KEY
}
    
model_id = "mistralai/mistral-medium-2505"

parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 1024
}

model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=PROJECT_ID
)


def speech_to_text(audio_binary):
    base_url = 'https://sn-watson-tts.labs.skills.network'
    api_url = base_url + '/speech-to-text/api/v1/recognize'

    # Parameters for HTTP request
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


def watsonx_process_message(user_message):
    # Set the prompt for Watsonx API, using a strict translation instruction
    prompt = f"""
        Translate the following English sentence into Spanish. 
        Reply ONLY with the translation, no explanations, no formatting, no extra text.

        English: {user_message}
        Spanish:
    """
    response_text = model.generate_text(prompt=prompt)
    return response_text.strip()
