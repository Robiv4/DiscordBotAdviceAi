import discord
import requests
import json
import os
from openai import OpenAI

def generate_joke():
    client = OpenAI(api_key="YOUR_API_KEY")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "generate a good advice to life"},
        ],
    )
    return completion.choices[0].message.content

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$advice'):
      await message.channel.send(generate_joke())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('DC-BOT-TOKEN')
