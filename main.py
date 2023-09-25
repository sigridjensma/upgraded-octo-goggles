# Importing required modules
import os
import discord
from dotenv import load_dotenv


intents = discord.Intents.default()
# intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)


@client.event   # iedere message die wordt gestuurd wordt naar de console gestuurd, ter controle
async def on_message(message):
    print(message.content)


@client.event   # guild count (in hoeveel guilds zit deze bot)
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("Jack Black is in " + str(guild_count) + " guilds.")


@client.event   # start van het spel, op het moment dat de user wil spelen
async def on_message(message):
    if message.content.find("/play") != -1:
        await message.channel.send("oke, je wil met mij blackjacken")


load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
