#Module
import discord
from discord.ext import commands

#Prefix bot is '.'
client = commands.Bot(command_prefix=".")
TOKEN = "YOUR TOKEN HERE"

#MAIN
@client.event
async def on_ready():
    print("Bot is Online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Spotify"))

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

client.run(TOKEN, bot=True)
