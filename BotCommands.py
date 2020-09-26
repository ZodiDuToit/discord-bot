import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name="members", help="returns a list of server's members")
async def members(ctx):

    await ctx.send(ctx.guild.members)

