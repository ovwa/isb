#Import modules.
import os
import discord
import discord.utils
import random
from discord.ext import commands

#Prefix.
client = commands.Bot(command_prefix="$", case_insensitive=True)

#Load commands (aka cogs).
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#This allows Isabelle to log in and act as vice president!
client.run(TOKEN)
