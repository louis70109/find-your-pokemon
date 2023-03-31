import unittest
from unittest.mock import patch
from utils.openai import generate_random_image


class TestGenerateRandomImage(unittest.TestCase):

    @patch("utils.openai.openai.Image.create")
    def test_generate_random_image(self, mock_create):
        mock_create.return_value = {"data": [{"url": "http://test_url.com"}]}
        pokemon_name = "Pikachu"
        result = generate_random_image(pokemon_name)
        mock_create.assert_called_with(
            prompt=f"3D render of a cute pokemon of {pokemon_name} in an aquarium on a dark blue background, digital art",
            n=1,
            size="1024x1024"
        )
        self.assertEqual(result, "http://test_url.com")
