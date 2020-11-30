#Import modules.
import os
import discord
import discord.utils
import random
from discord.ext import commands
from discord.ext.commands import has_role

#Cog creation
class Activation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        return

    #Simple hello command
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello!')
    
    #Impulse simpulse command
    @commands.command(aliases=['imp'])
    async def impulse(self, ctx):
        await ctx.send('impulse more like simpulse')

    #Spotify main command | doesn't point to a specific playlist
    @commands.group(invoke_without_command=True)
    async def spotify(self, ctx):
        await ctx.send('https://spoti.fi/33vgIyZ ♡')

    #Spotify sub command | points to the apex playlist
    @spotify.command()
    async def apex(self, ctx):
        await ctx.send('https://spoti.fi/2Jp981x, you can add music to this! ♡')

    #Discord link command
    @commands.command(aliases=['d', 'invite', 'inv'])
    async def discord(self, ctx):
        await ctx.send('use this link to invite friends! https://discord.gg/ZvkghTn ♡')
    
    #Youtube link command
    @commands.command(aliases=['yt'])
    async def youtube(self, ctx):
        await ctx.send('https://www.youtube.com/c/sukrit ♡')
    
    #Twitter link command
    @commands.command(aliases=['tw'])
    async def twitter(self, ctx):
        await ctx.send('https://www.twitter.com/suukriit ♡')
    
    #Twitter link command
    @commands.command(aliases=['ttv'])
    async def twitch(self, ctx):
        await ctx.send('https://www.twitch.tv/suukriit ♡')

    #Help Command
    @commands.command(aliases=['commands', 'cmds'])
    async def halp(self, ctx):
        #landlord = discord.utils.get(ctx.guild.roles, name="Landlord")
        #neighbor = discord.utils.get(ctx.guild.roles, name="Neighbor")
        #suki = discord.utils.get(ctx.guild.roles, name="Suki")
        person = ctx.message.author
        await ctx.message.delete()
        await ctx.channel.send(f"💌 | {person.mention}, check your dms love!", delete_after=4)
        embed = discord.Embed(colour=discord.Colour(0xaa6150), url="https://discordapp.com", description="꒰♡꒱ Isabelle is coded and is currently running on Python 3.9 and created by suki.\n \n**PREFIX** — $")
        embed.set_thumbnail(url="https://i.imgur.com/0x7Lr7R.jpg")
        embed.set_author(name="⌦ ISABELLE OS", icon_url="https://i.imgur.com/CD0ioXT.jpg")
        embed.add_field(name="**SOCIALS**", value="twitch\ntwitter\ndiscord\nyoutube\nspotify", inline=True)
        embed.add_field(name="**FUN**", value="impulse\nsqueak\nstealing?", inline=True)
        embed.add_field(name="**REPORTS**", value="ring\nclose", inline=True)
        await person.send(embed=embed)

#await operator.send("⌦ **ISABELLE. | SUKI**\n \n꒰ ♡ ꒱ Isabelle is operated and coded in `Python`, currently running on Python 3.9, created by sukrit#1975.\n \n**COMMANDS** ($)\n*conversational — activated w/o a prefix*\n \n'hey (isabelle/izzy) what cheese should i eat today' 'squeak'\nisabelle responds with a random cheese for you.\n \n*looks like so far there's no more commands available*")

def setup(client):
    client.add_cog(Activation(client))
