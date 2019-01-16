import discord
from discord.ext import commands
from discord.ext.commands import bot
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
    
bot.run(os.getenv.TOKEN)
