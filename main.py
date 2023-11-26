# Importing required modules
from discord.ext.commands import bot
from dotenv import load_dotenv
import os
import discord
import random
import time


# global repeat #  deze hoeft alleen maar als de repeat functie later wordt gebruikt.


intents = discord.Intents.default()
# intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)


# functie om te bekijken of de bot werkt.
# @client.event   # iedere message die wordt gestuurd wordt naar de console gestuurd, ter controle
# async def on_message(message):
#     print(message.content)


@client.event   # guild count
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("Jack Black is in " + str(guild_count) + " guilds.")


def pickcard(): # function to draw cards.
    global deck
    x = random.randint(0, (len(deck) - 1))
    card = deck[x]
    deck.pop(x) # prevents drawing the same card twice
    return card


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith("/play"):
        global gameactive
        gameactive = False
        repeat = True
        while repeat is True:  # this is here, in case the feature to play the game again is added
            if gameactive is True:  # fix being able to play two games at the same time
                return
            elif gameactive is False:
                # this line is the correct line for the game
                await message.channel.send(f"Oke {message.author}, je wilt blackjacken.")
                global deck  # unables you to take double cards
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
                global total  # total of users cards
                global compcards  # total of the computer's cards
                global ending  # enables the ending stage of the game
                ending = False
                # N = 1
                time.sleep(1)  # prevents the bot spamming messages
                await message.channel.send(f"De computer trekt eerst een kaart")
                card1computer = pickcard()
                card2computer = pickcard()
                compcards = [card1computer, card2computer]
                time.sleep(1)
                await message.channel.send(f"De eerste kaart van de computer is: {card1computer}")
                time.sleep(1)
                await message.channel.send(f"De tweede kaart van de computer krijg je aan het einde van het" +
                                           f" spel te zien")
                time.sleep(1)
                await message.channel.send(f"Nu mag jij 2 kaarten trekken.")
                card1player = pickcard()
                card2player = pickcard()
                total = card1player + card2player
                time.sleep(1)
                await message.channel.send(f"Je hebt een {card1player} getrokken, en je hebt een {card2player} " +
                                           f"getrokken.\nJe totaal is nu {total}")
                if total >= 21:
                    ending = True
                else:
                    ending = False
                while ending is False:
                    time.sleep(1)
                    await message.channel.send(f"Wil jij nog een kaart?")  # probleem is dat hij voor onderstaande
                    # invoercorrectie de /play command gebruikt waarmee de code wordt aangeroepen.
                    goodinput = False
                    takingcard = await bot.wait_for_message(author=message.author)  # deze werkt niet. Hiet zit ook het
                    # probleem van de code, aangezien dit het punt is dat de code vastloopt. Hij moet wachten met ver
                    # dergaan, omdat hij anders dus de /play command gaat gebruiken. ik krijg dit niet voor elkaar
                    while goodinput is False:  # checking the input
                        print(message.content)
                        if takingcard == "ja":  # if answer is yes
                            card = pickcard()
                            total = total + card
                            time.sleep(1)
                            await message.channel.send(f"Jij hebt getrokken {card} /n Je totaal is nu {total}")
                            goodinput = True
                        elif takingcard == "nee":  # if answer is no
                            await message.channel.send(f"Oke.")
                            goodinput = True
                        else:  # if answer is nor 'yes' or 'no'
                            time.sleep(1)
                            await message.channel.send(f"Beantwoord met ja of nee")
                            time.sleep(3)
                            goodinput = False
                    if total >= 21:  # if user has 21, game goes to endingstage
                        ending = True
                    else:
                        ending = False
                # starting ending phase
                winnerchosen = False
                global computertotal  # same as earlier
                global winner
                card1computer = compcards[0]  # getting the cards out of the list made earlier
                card2computer = compcards[1]
                computertotal = card1computer + card2computer
                time.sleep(1)
                await message.channel.send(f"De computer had als tweede kaart {card2computer} en dus een totaal" +
                                           f"van {computertotal}")  # reveal computer's total
                while computertotal < 17:  # if computertotal is smaller than 17, it gets to draw more cards
                    computercard = pickcard()
                    computertotal = computertotal + computercard
                time.sleep(1)
                await message.channel.send(f"De computer heeft nu als totaal: {computertotal}")
                if total > 21:  # if player's total is bigger than 21 = instant lose
                    winner = 1  # 1 is computer
                    time.sleep(1)
                    await message.channel.send(f"Je had hoger dan 21")
                    winnerchosen = True
                if computertotal > 21:  # if the computer has more than 21, you win
                    if total > 21:  # except if you also got 21, then the computer wins.
                        winner = 1  # computer
                        await message.channel.send("De computer had 21, maar jij ook.")
                    else:
                        winner = 2  # player
                        await message.channel.send("De computer had 21.")
                    time.sleep(1)
                    winnerchosen = True
                if total == 21:  # if you had a total of 21
                    if computertotal == 21:  # if the computer also had 21, you lose
                        winner = 1
                        time.sleep(1)
                        await message.channel.send(f"De computer had een totaal van 21")
                        winnerchosen = True
                    else:  # if you had 21 and the computer too, you lose
                        winner = 2
                        time.sleep(1)
                        await message.channel.send(f"Je had 21 en de computer niet")
                        winnerchosen = True
                if winnerchosen is False:
                    if computertotal > total:
                        winner = 1  # computer
                        winnerchosen = True
                    if total > computertotal:
                        winner = 2  # player
                        winnerchosen = True
                if winner == 2:  # player is winner
                    time.sleep(1)
                    await message.channel.send(f"Gefeliciteerd, je hebt gewonnen")
                if winner == 1:  # computer is winner
                    time.sleep(1)
                    await message.channel.send(f"Jammer, je hebt verloren.")
                repeat = False
                time.sleep(1)
                # await message.channel.send(f"Wil je nog een potje spelen? ja of nee") # start of repeat function inactive for now
                # message2 = message.content.lower
                # goodinput = False
                # while goodinput is False:
                #     if message2 == "ja":
                #         repeat = True
                #         goodinput = True
                #     elif message2 == "nee":
                #         repeat = False
                #         time.sleep(1)
                #         await message.channel.send(f"Tot ziens")
                #         goodinput = True
                #     else:
                #         time.sleep(1)
                #         await message.channel.send(f"'ja' of 'nee' alsjeblieft.")
                #         goodinput = False
                gameactive = False
            else:
                return

            # communicatie
            # repeat als speler dat wil.


load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)


# dit is allemaal oude code. werkte alleen niet bij een asynchrone functie.
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