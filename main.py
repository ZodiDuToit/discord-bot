
import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('')

bot = commands.Bot(command_prefix='!')
client = discord.Client

#on ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#PUBLIC COMMANDS --------------------------------



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

async def unban(ctx, member):
    
    banned_users = await ctx.guild.bans()
    print(banned_users)
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):

            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            
            user.send(f"You have been unbanned from {ctx.guild}")
            break

# ERROR HANDLING ---------------------------------
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role/permissions for this command.')


bot.run(TOKEN)

    