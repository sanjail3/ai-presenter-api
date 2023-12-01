from pexels_api import API
import requests
import os
from dotenv import load_dotenv


# Load environment variables from .env file



def get_image(topic):
    load_dotenv()
    pixel_api = os.getenv("PEXELS_API_KEY")

    # Access the secret key from the environment variable



    pexels_api = API(pixel_api)

    if not os.path.exists('images'):
        os.makedirs('images')
    photos = pexels_api.search(topic)
    for index, photo in enumerate(photos['photos'], start=1):
        image_url = photo['src']['large']
        image_id = photo['id']
        image_filename = f'images/{index}.jpg'  # Save the images in the "images" directory

        response = requests.get(image_url)
        response.raise_for_status()

        with open(image_filename, 'wb') as file:
            file.write(response.content)

        print(f"Image saved: {image_filename}")
