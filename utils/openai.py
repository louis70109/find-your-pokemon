import os
import openai
import logging

logger = logging.getLogger(__file__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_random_image(pokemon: str) -> str:
    response = openai.Image.create(
        prompt=f"{pokemon}, Japon cine, Japan cine poster 1985, realistic --ar 15:22",
        n=1,
        size="1024x1024"
    )
    logger.debug('OpenAI URL is: %s', response['data'][0]['url'])
    return response['data'][0]['url']


def generate_openai_prompt(prompt: str) -> str:
    promt_str = f"""
    你是一位寶可夢專家(Pokemon Expert)，選用「{prompt}」，
    請你列點式給出適合這篇文案的撰寫大綱架構，使用 markdown 格式顯示，
    請用分段的樣式讓最終答案的文字視覺看起來順暢，
    但不用使用 code mode。
    整篇文長約 1,000 個中文字，
    文章中不應該有網頁標籤、html tag、 "fluff"、充數用而沒有實質價值的廢話。
    請列點：

    Please write in the Traditional Chinese language.
    """
    return openai.Completion.create(model="text-davinci-003", prompt=promt_str, temperature=0, max_tokens=7)
