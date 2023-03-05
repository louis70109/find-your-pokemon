import os
import openai
import logging

logger = logging.getLogger(__file__)

def generate_random_image(pokemon):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Image.create(
        prompt=f"a pancil drawing pokemon of {pokemon} wait for challenge",
        n=1,
        size="1024x1024"
    )
    logger.debug('URL is: %s', response['data'][0]['url'])
    return response['data'][0]['url']
