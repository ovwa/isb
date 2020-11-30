#Import modules.
import os
import discord
import discord.utils
import random
from discord.ext import commands

#Cog creation
class Filter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        bw = (
        'tranny',
        'faggot',
        'slave',
        'nigga',
        'nigger',
        'trump',
        'tr@nny',
        'f@ggot',
        'fag',
        'f@g',
        'n1gg@',
        'n1gga',
        'n!gg@',
        'n!gga'
        )
        bm = {}
        user = message.author.id

        if any([True if i in message.content else False for i in bw]):
            await message.delete()
            await message.channel.send("no ma'am!")
        try:
            if message.content.lower() in bm[user]:
                await message.delete()
                await message.channel.send("no ma'am!")
        except KeyError:
            bm[user] = []
        finally:
            bm[user].append(message.content.lower())

def setup(client):
    client.add_cog(Filter(client))
