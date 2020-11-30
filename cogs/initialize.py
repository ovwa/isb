#Modules
import discord
from discord.ext import commands

#Cog creation
class Initialize(commands.Cog):

# _____ _____ _____ _____ _____ __    __    _____    _____ _____ 
#|     |   __|  _  | __  |   __|  |  |  |  |   __|  |     |   __|
#|-   -|__   |     | __ -|   __|  |__|  |__|   __|  |  |  |__   |
#|_____|_____|__|__|_____|_____|_____|_____|_____|  |_____|_____|

#“Good morning, Mayor!”

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="villagers."))
        print(' _____ _____ _____ _____ _____ __    __    _____    _____ _____ \n|     |   __|  _  | __  |   __|  |  |  |  |   __|  |     |   __|\n|-   -|__   |     | __ -|   __|  |__|  |__|   __|  |  |  |__   |\n|_____|_____|__|__|_____|_____|_____|_____|_____|  |_____|_____|\n \n                     “Good morning, Mayor!”')

def setup(client):
    client.add_cog(Initialize(client))

