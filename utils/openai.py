import os
import openai
import logging

logger = logging.getLogger(__file__)

def generate_random_image(pokemon: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Image.create(
        prompt=f"3D render of a cute pokemon of {pokemon} in an aquarium on a dark blue background, digital art",
        n=1,
        size="1024x1024"
    )
    logger.debug('URL is: %s', response['data'][0]['url'])
    return response['data'][0]['url']
