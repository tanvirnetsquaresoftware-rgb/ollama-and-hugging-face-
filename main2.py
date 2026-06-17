import ollama 
response=ollama.chat(
    model="llama3.2",
    messages=[{
        "role":"user",
        "content":"explain AI in three lines "
    }]
)

print(response["message"]["content"])