from openai import OpenAI
import os 
from dotenv import find_dotenv, load_dotenv

from openai import OpenAI
OPENAI_API_KEY='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'
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.images.generate(
    prompt="A cute baby sea otter",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)

