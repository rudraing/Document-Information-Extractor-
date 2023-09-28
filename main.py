import openai
import chainlit as cl
import os

os.environ['OPENAI_API_KEY'] ="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"
openai.api_key="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"
#return everything that user inputs
@cl.on_message
async def main(message :str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "You are a helpful assistant who is obsessed with potatoes."},
            {"role":"user","content":message}
        ],
        temperature=1,
    )
    await cl.Message(content=f"{str(response['choices'][0]['message']['content'])}",).send()
