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
        def dados():
            m1 = message.content[1]
            m2 = message.content[2]
            if m1.startswith("d"):
                dices = 0
                i = 0
                while dices < int(first_letter):
                    dice6 = randint(1, m2)
                    diceArray[i] = dice6
                    dices += 1
                    i += 1
                formatted_list = ", ".join(map(str, diceArray))
                message.channel.send("```" + first_letter + f"d" + m2 + " -> [" + formatted_list + "]```")

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)
client.run('')