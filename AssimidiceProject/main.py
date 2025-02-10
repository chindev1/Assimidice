import discord
from random import randint


class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if len(message.content) > 0 and message.content[0].isdigit():
            first_letter = message.content[0]

            diceArray = [None] * int(first_letter)
            img_file = None  # Inicializa a variável da imagem

            async def dados():
                if len(message.content) > 2 and message.content[1] == "d":
                    m2 = message.content[2:]
                    try:
                        m2 = int(m2)
                    except ValueError:
                        return

                    dices = 0
                    i = 0
                    while dices < int(first_letter):
                        dice6 = randint(1, m2)
                        diceArray[i] = dice6

                        # Verifica se o dado atual é 3 e define a imagem
                        if dice6 == 3 and not img_file:
                            await message.channel.send(
                                img_file=discord.File('dice3.PNG')
                            )
                        elif dice6 == 4:
                            await message.channel.send(
                                file=discord.File('dice4.PNG')
                            )
                        elif dice6 == 5:
                              # Mantém apenas a primeira ocorrência
                            await message.channel.send(

                                file=discord.File('dice5.PNG')
                            )
                        elif dice6 == 6:
                            await message.channel.send(
                                file=discord.File('dice6.PNG')
                            )
                        elif dice6 == 7:
                            await message.channel.send(
                                file=discord.File('dice7.PNG')
                            )
                        elif dice6 == 8:
                            await message.channel.send(
                                file=discord.File('dice8.PNG')
                            )
                        elif dice6 == 9:
                            await message.channel.send(
                                file=discord.File('dice9.PNG')
                            )
                        elif dice6 == 10:
                            await message.channel.send(
                                file=discord.File('dice10.PNG')
                            )
                        elif dice6 == 11:
                            await message.channel.send(
                                file=discord.File('dice11.PNG')
                            )
                        elif dice6 == 12:
                            await message.channel.send(
                                file=discord.File('dice12.PNG')
                            )
                        else:
                            await message.channel.send("Rolagem bem sucedida!!")
                        dices += 1
                        i += 1

                    formatted_list = ", ".join(map(str, diceArray))

                    # Envia com imagem se houver pelo menos um 3
                    if img_file:
                        await message.channel.send(
                            f"```{first_letter}d{m2} -> [{formatted_list}]```",
                            file=img_file
                        )
                    else:
                        await message.channel.send(f"```{first_letter}d{m2} -> [{formatted_list}]```")

            await dados()


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('INSERT DISCORD TOKEN')