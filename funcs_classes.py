import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    await ctx.send(response)

bot.run(TOKEN)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.channel.send("hi")

@client.event
async def on_member_join(member):

    await member.create_dm()
    await member.dm_channel.send(
        f'Everybody pleas welcome {member.name}'
    )

def get_members():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    members = [member.name for member in guild.members]


    