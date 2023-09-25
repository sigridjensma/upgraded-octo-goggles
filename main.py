# Importing required modules
import os
import discord
import random
global repeat
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


def pickcard():
    global deck
    x = random.randint(0, (len(deck) - 1))
    card = deck[x]
    deck.pop(x)
    return card


def init():  # begin van het spel
    global deck  # zo kan je geen dubbele kaarten trekken
    deck = [2, 2, 2, 2,
            3, 3, 3, 3,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10, 10,  # de 10
            10, 10, 10, 10,  # de boer
            10, 10, 10, 10,  # de vrouw
            10, 10, 10, 10,  # de koning
            11, 11, 11, 11]  # de aas
    # global N
    global total  # het totaal van users kaarten
    global compkaarten  # het totaal van de computers kaarten
    global ending # het einde van het spel
    ending = False
    # N = 1
    message.channel.send("De computer trekt eerst een kaart")
    kaart1computer = pickcard()
    kaart2computer = pickcard()
    compkaarten = [kaart1computer, kaart2computer]
    message.channel.send("De eerste kaart van de computer is:", kaart1computer
    "/n De tweede kaart van de computer krijg je aan het einde van het spel te zien")
    message.channel.send("Nu mag jij 2 kaarten trekken.")
    kaart1speler = pickcard()
    kaart2speler = pickcard()
    total = kaart1speler + kaart2speler
    message.channel.send("Je hebt een", kaart1speler, "getrokken, en je hebt een", kaart2speler,
                         "getrokken. \n Je totaal is nu", total)
    if total >= 21:
        ending = True
    else:
        ending = True


def round():
    global total
    global ending
    message.channel.send("Wil jij een nog een kaart?")
    message2 = message.content.lower()
    inputcorrection = False
    while inputcorrection == False:
        message.channel.send("Wil jij een nog een kaart?")
        message2 = message.content.lower()
        if message2 == "ja":
            card = pickcard()
            total = total + card
            message.channel.send("Jij hebt getrokken", card, "/n Je totaal is nu", total)
            inputcorrection = True
        elif message2 == "nee":
            message.channel.send("Oke.")
            inputcorrection = True
        else:
            message.channel.send("Beantwoord met ja of nee")
    if total >= 21:
        ending = True
    else:
        ending = False


def closingstage():
    kaart1computer = compkaarten[0]
    kaart2computer = compkaarten[1]
    computertotal = kaart1computer + kaart2computer
    if total > 21:
        message.channnel.send("Helaas, je hebt verloren.")
    # hier moet de computers kaart worden revealed
    kaart1computer = compkaarten[0]
    kaart2computer = compkaarten[1]
    computertotal = kaart1computer + kaart2computer
    message.channel.send("De computer had als tweede kaart", kaart2computer, "en dus een totaal van", computertotal)
    # hier moet de computer verder trekken (eventueel,)






@client.event   # start van het spel, op het moment dat de user wil spelen
async def on_message(message):
    if message.content.startswith("/play") != -1:
        global spelactief
        if spelactief == True:
            return
        else:
            await message.channel.send("oke, je wil met mij blackjacken")
            init()
            while ending == False:
                round()




load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
