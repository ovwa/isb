#Import modules.
import os
import discord
import discord.utils
import random
from discord.ext import commands

#Cog creation
class Converse(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        client = self.client

        if message.author == client.user:
            return

        #Cheese commands

        if str(message.content).lower() == ('hey isabelle what cheese should i eat today'):
            cheeses = ["cheetos", "parmesean", "gouda", "cheddar", "mozzarella", "colby Jack", "pepper jack", "cream cheese", "brie", "teleme", "feta", "blue", "goat's cheese"]
            result = random.choice(cheeses)
            await message.channel.send(result)
            return

        if str(message.content).lower() == ('hey izzy what cheese should i eat today'):
            cheeses = ["cheetos", "parmesean", "gouda", "cheddar", "mozzarella", "colby Jack", "pepper jack", "cream cheese", "brie", "teleme", "feta", "blue", "goat's cheese"]
            result = random.choice(cheeses)
            await message.channel.send(result)
            return

        if str(message.content).lower() == ('squeak'):
            cheeses = ["cheetos", "parmesean", "gouda", "cheddar", "mozzarella", "colby Jack", "pepper jack", "cream cheese", "brie", "teleme", "feta", "blue", "goat's cheese"]
            result = random.choice(cheeses)
            await message.channel.send(result)
            return

        #Stealing? Good
        
        if str(message.content).lower() == ('stealing? good'):
            await message.channel.send('stealing? good')
            return
        
        if str(message.content).lower() == ('stealing?'):
            await message.channel.send('good')
            return

def setup(client):
    client.add_cog(Converse(client))
