import discord
import os


TOKEN = os.getenv('TEST_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    #channel = client.get_channel(812906949124423700)
    if message.author == client.user:
        return
    else:
        await message.channel.send('Heya')

client.run(TOKEN)