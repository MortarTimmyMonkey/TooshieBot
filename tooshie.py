import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import os

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
	print("Ready")
	
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"Pong! {ping}ms")

@bot.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if member == None:
        await ctx.channel.send("No member at all!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been banned from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")
    
bot.run(os.getenv('TOKEN'))
