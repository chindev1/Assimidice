from random import randint

import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
    async def on_message(self, message):
        first_letter = message.content[0]

        diceArray = [None] * int(first_letter)
        diceArray[1] = 0

        #print(f"Message from {message.author}: {message.content}")
        if message.author == self.user:
            return

        if message.content[1].startswith("d") and message.content[2].startswith("6"):
            dices = 0
            i = 0
            while dices < int(first_letter):
                dice6 = randint(1, 6)
                diceArray[i] = dice6
                dices += 1
                i += 1
            formatted_list = ", ".join(map(str, diceArray))
            await message.channel.send("```" + first_letter + f"d6 -> [" + formatted_list + "]```")


        if message.content[1].startswith("d") and message.content[2].startswith("2") and message.content[3].startswith("0"):
            dices = 0
            i = 0
            while dices < int(first_letter):
                dice6 = randint(1, 20)
                diceArray[i] = dice6
                dices += 1
                i += 1
            formatted_list = ", ".join(map(str, diceArray))
            await message.channel.send("```" + first_letter + f"d20 -> [" + formatted_list + "]```")


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)
client.run('')