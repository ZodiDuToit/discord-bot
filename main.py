import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')

bot = commands.Bot(command_prefix='!')
client = discord.Client

#on ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#PUBLIC COMMANDS --------------------------------

@bot.command(name='ping', help="the bot will respond with 'pong ' if online")
async def ping(ctx):
    await ctx.channel.send("pong")

#ADMIN COMMANDS ---------------------------------

# create channel
@bot.command(name='create-channel', help="creates a new text channel")
@commands.has_permissions(administrator= True)

async def create_channel(ctx, channel_name):

    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels,name=channel_name)

    if not existing_channel and len(channel_name) > 0:

        print(f'Creating a new channel: {channel_name}')

        await ctx.send("Creating a new channel: " + channel_name)
        await guild.create_text_channel(channel_name)

# kick member
@bot.command(name="kick", help="kicks a member")
@commands.has_permissions(kick_members=True)

async def kick(self, ctx, member: discord.Member, reason=None):

    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked, reason: {reason}')

# ban member
@bot.command(name="ban", help="bans member(s)")
@commands.has_permissions(ban_members=True)

async def ban (ctx, member:discord.User=None, reason=None):
    if member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return

    if member == None:
        await ctx.channel.send("You can't use banning like that")

    message = f"You have been banned from {ctx.guild.name} for {reason}"

    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")


# unban member
@bot.command(name="unban", help="unbans member")
@commands.has_permissions(administrator=True)

async def unban(ctx, member: discord.User= None):

    await ctx.guild.unban(member)
    await ctx.send(f'Unbanned {member.name}')

    member.send(f"You have been unbanned from {ctx.guild}")
    
# ERROR HANDLING ---------------------------------
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role/permissions for this command.')

bot.run(TOKEN)
    