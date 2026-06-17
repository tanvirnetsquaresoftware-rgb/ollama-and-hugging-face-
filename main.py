from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\Tanul\OneDrive\Desktop\intern\JUNE 17\api.env")

api_key=os.getenv("api_key")

client=InferenceClient(
    token=api_key
)

response=client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role":"user",
            "content":"Explain AI in 3 lines"
        }
    ],
    max_tokens=100
)

print(response.choices[0].message.content)