import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://openai-merito.openai.azure.com/",
    api_key=os.getenv("AZURE_OPENAI_KEY"),
)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Powiedz coś po polsku."}],
    model='gpt-4o'
)

print(response.choices[0].message.content)