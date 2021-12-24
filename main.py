import discord
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

token = os.environ.get("TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("Standing by...")

@client.event
async def on_message(message):
    if message.author.id == :
        await message.channel.send("https://media1.giphy.com/media/IDGNYvFLkJKLK/giphy.gif?cid=ecf05e47u8uggyhua9oidbpct0y8fd4twggl69m7if69ua8p&rid=giphy.gif&ct=g")

client.run(token)
