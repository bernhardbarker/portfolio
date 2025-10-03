"""
Image captioning tool using the BLIP model from Hugging Face's Transformers

From course: Building Generative AI-Powered Applications with Python, module 1
https://www.coursera.org/learn/building-gen-ai-powered-applications/ungradedLti/tFwmk/lab-babel-fish-language-translator-with-llm-stt-tts
"""
from io import BytesIO
import requests
from flask import Flask
from PIL import Image
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

app = Flask(__name__)

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

TIMEOUT = 20


@app.route('/get/<path:url>', methods=['GET'])
def get_captions_from_url(url):
    """ Endpoint to get caption for URL's images """
    output = ""

    # Set user agent for Wikipedia
    headers = {'User-Agent': 'BlipImageCaptioningBot/0.0'}

    # Download the page
    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    if not response.ok:
        raise ValueError(f"Fetch error: {response.status_code} - {response.text}")

    # Find and iterate over all images
    for img_element in soup.find_all('img'):
        img_url = img_element.get('src')
        print("Getting", img_url)

        # Skip if the image is an SVG or too small (likely an icon)
        if 'svg' in img_url or '1x1' in img_url:
            continue

        # Correct the URL if it's malformed
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http://') and not img_url.startswith('https://'):
            continue  # Skip URLs that don't start with http:// or https://

        try:
            # Download the image
            response = requests.get(img_url, headers=headers, timeout=TIMEOUT)
            if not response.ok:
                raise ValueError(f"Image download error: {response.status_code} - {response.text}")

            # Convert the image data to a PIL Image
            raw_image = Image.open(BytesIO(response.content))
            if raw_image.size[0] * raw_image.size[1] < 400:  # Skip very small images
                continue

            raw_image = raw_image.convert('RGB')

            # Process the image
            inputs = processor(raw_image, return_tensors="pt")
            # Generate a caption for the image
            out = model.generate(**inputs, max_new_tokens=50)
            # Decode the generated tokens to text
            caption = processor.decode(out[0], skip_special_tokens=True)

            # Append the image and caption to the output
            output += f'<img src="{img_url}"><br>{caption}<br><br>'
        except Exception as e:
            print(f"Error processing image {img_url}: {e}")
            continue

    return output


if __name__ == '__main__':
    app.run(port=5002)


# Example URL: http://127.0.0.1:5002/get/https://en.wikipedia.org/wiki/IBM
# Shows images with generated captions
