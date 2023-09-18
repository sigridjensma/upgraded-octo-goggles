# Importing required modules
import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
#intents.typing = False
intents.presences = False
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client(intents=intents)
client.run(TOKEN)
