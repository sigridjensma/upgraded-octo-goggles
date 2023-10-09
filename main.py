# Importing required modules
from dotenv import load_dotenv
import os
import discord
import random
global repeat


intents = discord.Intents.default()
# intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)


@client.event   # iedere message die wordt gestuurd wordt naar de console gestuurd, ter controle
async def on_message(message):
    print(message.content)
    await message.channel.send("Fuck ha")


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


# def init():  # begin van het spel
#     global deck  # zo kan je geen dubbele kaarten trekken
#     deck = [2, 2, 2, 2,
#             3, 3, 3, 3,
#             4, 4, 4, 4,
#             5, 5, 5, 5,
#             6, 6, 6, 6,
#             7, 7, 7, 7,
#             8, 8, 8, 8,
#             9, 9, 9, 9,
#             10, 10, 10, 10,  # de 10
#             10, 10, 10, 10,  # de boer
#             10, 10, 10, 10,  # de vrouw
#             10, 10, 10, 10,  # de koning
#             11, 11, 11, 11]  # de aas
#     # global N
#     global total  # het totaal van users kaarten
#     global compkaarten  # het totaal van de computers kaarten
#     global ending   # het einde van het spel
#     ending = False
#     # N = 1
#     message.channel.send(f"De computer trekt eerst een kaart")
#     kaart1computer = pickcard()
#     kaart2computer = pickcard()
#     compkaarten = [kaart1computer, kaart2computer]
#     message.channel.send("De eerste kaart van de computer is:", kaart1computer)
#     message.channel.send("/n De tweede kaart van de computer krijg je aan het einde van het spel te zien")
#     message.channel.send(f"Nu mag jij 2 kaarten trekken.")
#     kaart1speler = pickcard()
#     kaart2speler = pickcard()
#     total = kaart1speler + kaart2speler
#     message.channel.send(f"Je hebt een", kaart1speler, "getrokken, en je hebt een", kaart2speler,
#                          "getrokken. \n Je totaal is nu", total)
#     if total >= 21:
#         ending = True
#     else:
#         ending = False
#
#
# def round():
#     global total
#     global ending
#     message.channel.send(f"Wil jij een nog een kaart?")
#     message2 = message.content.lower() #communicatie
#     inputcorrection = False
#     while inputcorrection is False:
#         message.channel.send(f"Wil jij een nog een kaart?")
#         message2 = message.content.lower()
#         if message2 == "ja":
#             card = pickcard()
#             total = total + card
#             message.channel.send(f"Jij hebt getrokken", card, "/n Je totaal is nu", total)
#             inputcorrection = True
#         elif message2 == "nee":
#             message.channel.send(f"Oke.")
#             inputcorrection = True
#         else:
#             message.channel.send(f"Beantwoord met ja of nee")
#     if total >= 21:
#         ending = True
#     else:
#         ending = False


# def closingstage():
#     winnerchosen = False
#     global computertotal
#     kaart1computer = compkaarten[0]
#     kaart2computer = compkaarten[1]
#     computertotal = kaart1computer + kaart2computer
#     kaart1computer = compkaarten[0]
#     kaart2computer = compkaarten[1]
#     computertotal = kaart1computer + kaart2computer
#     message.channel.send(f"De computer had als tweede kaart", kaart2computer, "en dus een totaal van", computertotal)
#     while computertotal < 17:
#         computerkaart = pickcard()
#         computertotal = computertotal + computerkaart
#     message.channel.send(f"De computer heeft nu als totaal:", computertotal)
#     if total > 21:
#         winner = 1
#         message.channel.send(f"Je hebt verloren, je had hoger dan 21")
#         winnerchosen = True
#     if computertotal > 21:
#         winner = 2
#         message.channel.send(f"Je hebt gewonnen, want de computer had hoger dan 21")
#         winnerchosen = True
#     if total == 21:
#         if computertotal == 21:
#             winner = 1
#             message.channel.send(f"De computer heeft gewonnen, want hij had een totaal van 21")
#             winnerchosen = True
#         else:
#             winner = 2
#             message.channel.send(f"Jij hebt gewonnen, want je had 21 en de computer niet")
#             winnerchosen = True
#     while winnerchosen is False:
#         if computertotal > total:
#             winner = 1
#         if total > computertotal:
#             winner = 2
#     if winner == 2:
#         message.channel.send(f"Gefeliciteerd, je hebt gewonnen")
#     if winner == 1:
#         message.channel.send(f"Jammer, je hebt verloren.")


# @client.event   # start van het spel, op het moment dat de user wil spelen
# async def on_message(message):
#     if message.content.startswith("/play") != -1:
#         repeat = True
#         while repeat is True:
#             global spelactief
#             if spelactief is True:
#                 return
#             else:
#                 await message.channel.send(f"oke, je wil met mij blackjacken")
#                 init()
#                 while ending is False:
#                     round()
#                 closingstage()
#                 repeat = False
#                 message.channel.send(f"Wil je nog een keer spelen?")
#                 # insert communicatie + invoercorrectie
#                 if answer1 == "ja":
#                     repeat = True
#                 elif answer1 == "nee":
#                     repeat = False
#                 else:
#                     message.channel.send(f"graag ja of nee")
#                 spelactief = False


@client.event
async def on_message(message):
    if message.content.startswith("/play") != -1:
        global spelactive
        repeat = True
        while repeat is True:
            if spelactive is True:
                return
        else:
            await message.channel.send("Oke, je wilt blackjacken.")
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
            global ending  # het einde van het spel
            ending = False
            # N = 1
            message.channel.send(f"De computer trekt eerst een kaart")
            kaart1computer = pickcard()
            kaart2computer = pickcard()
            compkaarten = [kaart1computer, kaart2computer]
            message.channel.send("De eerste kaart van de computer is:", kaart1computer)
            message.channel.send("/n De tweede kaart van de computer krijg je aan het einde van het spel te zien")
            message.channel.send(f"Nu mag jij 2 kaarten trekken.")
            kaart1speler = pickcard()
            kaart2speler = pickcard()
            total = kaart1speler + kaart2speler
            message.channel.send(f"Je hebt een", kaart1speler, "getrokken, en je hebt een", kaart2speler,
                                 "getrokken. \n Je totaal is nu", total)
            if total >= 21:
                    ending = True
            else:
                ending = False
        while ending is False:
            global total
            global ending
            message.channel.send(f"Wil jij een nog een kaart?")
            message3 = message.content.lower()  # communicatie
            goodinput = False
            while goodinput is False:
                message.channel.send(f"Wil jij een nog een kaart?")
                message3 = message.content.lower()
                if message3 == "ja":
                    card = pickcard()
                    total = total + card
                    message.channel.send(f"Jij hebt getrokken", card, "/n Je totaal is nu", total)
                    goodinput = True
                elif message3 == "nee":
                    message.channel.send(f"Oke.")
                    goodinput = True
                else:
                    message.channel.send(f"Beantwoord met ja of nee")
                    goodinput = False
            if total >= 21:
                ending = True
            else:
                ending = False
            winnerchosen = False
            global computertotal
            kaart1computer = compkaarten[0]
            kaart2computer = compkaarten[1]
            computertotal = kaart1computer + kaart2computer
            kaart1computer = compkaarten[0]
            kaart2computer = compkaarten[1]
            computertotal = kaart1computer + kaart2computer
            message.channel.send(f"De computer had als tweede kaart", kaart2computer, "en dus een totaal van",
                                 computertotal)
            while computertotal < 17:
                computerkaart = pickcard()
                computertotal = computertotal + computerkaart
            message.channel.send(f"De computer heeft nu als totaal:", computertotal)
            if total > 21:
                winner = 1
                message.channel.send(f"Je hebt verloren, je had hoger dan 21")
                winnerchosen = True
            if computertotal > 21:
                winner = 2
                message.channel.send(f"Je hebt gewonnen, want de computer had hoger dan 21")
                winnerchosen = True
            if total == 21:
                if computertotal == 21:
                    winner = 1
                    message.channel.send(f"De computer heeft gewonnen, want hij had een totaal van 21")
                    winnerchosen = True
                else:
                    winner = 2
                    message.channel.send(f"Jij hebt gewonnen, want je had 21 en de computer niet")
                    winnerchosen = True
            while winnerchosen is False:
                if computertotal > total:
                    winner = 1
                if total > computertotal:
                    winner = 2
            if winner == 2:
                message.channel.send(f"Gefeliciteerd, je hebt gewonnen")
            if winner == 1:
                message.channel.send(f"Jammer, je hebt verloren.")
            repeat = False
            message.channel.send("Wil je nog een potje spelen? ja of nee")
            message2 = message.content.lower
            goodinput = False
            while goodinput is False:
                if message2 == "ja":
                    repeat = True
                    goodinput = True
                elif message2 == "nee":
                    repeat = False
                    message.channel.send("Tot ziens")
                    goodinput = True
                else:
                    message.channel.send("'ja' of 'nee' alsjeblieft.")
                    goodinput = False

            # communicatie
            # repeat als speler dat wil.


load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
