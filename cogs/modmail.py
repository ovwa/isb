#Import modules.
import os
import discord
import discord.utils
import random
from discord.ext import commands

#Cog creation
class Modmail(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):

        #Defining the discord client and variables
        client = self.client
        ea = []
        mm = discord.utils.get(client.get_all_channels(), name="support")

        #Prevent an echo to the support channel
        if message.author == client.user:
            return

        #Check if it's a dm channel
        if str(message.channel.type) == "private":

            if message.attachments != ea: #Check if it's a file
                fi = message.attachments
                await mm.send("꒰ " + message.author.display_name + " ꒱ 𐐪 **attachment below** 𐑂")
                for file in fi:
                    await mm.send(file.url)

            else: #The instruction for dm reports is that they would say 'ring' to start a dm report
                if str(message.content).lower() == ('ring'):
                    await message.channel.send(":sparkles: | please describe your issue while i get an operator for you.")
                    #This would inturn notify operators that there is someone in need of support
                    await mm.send(f'🌞 | {message.author.display_name} is in need of a <@&781479463237189643>.') 
                else:
                    if str(message.content).lower() == ('close'): 
                        await message.channel.send("🏷 | thank you for contacting suki support, we hope we resolved your issue!")
                        await mm.send(f"🏷 | {message.author.mention} marked their support session as completed.")
                    else:
                        await mm.send("꒰ " + message.author.display_name + " ꒱: "+ message.content)

        elif str(message.channel) == "support" and message.content.startswith("<"):
            mo = message.mentions[0]
            
            #Check if it's a file
            if message.attachments != ea:
                fi = message.attachments
                for file in fi:
                    await mo.send("꒰ " + message.author.display_name + " ꒱ 𐐪 attachment below 𐑂")
                    await mo.send(file.url)
            else:
                index = message.content.index(" ")
                string = message.content
                mmsg = string[index:]
                if str(mmsg).lower() == (' connect'):
                    await mo.send("🎟 | alright, patching you through to an operator! (" + message.author.display_name + ")", delete_after=10)
                else:
                    if str(mmsg).lower() == (' close'):
                        await mo.send("🏷 | thank you for contacting suki support, we hope we resolved your issue! (your handler today was: " + message.author.display_name + ")")
                    else:
                        if str(mmsg).lower() == (' ar01'):
                            await mo.send("🌤 | unfortunately your issue isn't valid and/or related to suki's room.")
                        else:
                            if str(mmsg).lower() == (' ar02'):
                                await mo.send("🌤 | please respond with a valid issue or close your ticket by saying 'close'.") 
                            else:
                                await mo.send("🌤 | " + mmsg)


#🎟

def setup(client):
    client.add_cog(Modmail(client))
