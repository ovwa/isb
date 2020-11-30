#Import modules.
import os
import discord
import discord.utils
import random
import time
from discord.ext import commands

#Cog creation
class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.command() #Command aliases
    @commands.has_permissions(ban_members = True) #Check the message sender's permissions
    async def ban(self, ctx, member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Banished")
        mrole = discord.utils.get(ctx.guild.roles, name="Cutie")
        channel = ctx.guild.get_channel(780504308004290601)
        operator = ctx.message.author
        await ctx.channel.send(f"⛈ | successfully banned {member.mention}.", delete_after=4)
        await channel.send(f"⛈ | {operator.mention} successfully banned {member.mention}.")
        await member.add_roles(role)
        await time.sleep(1)
        await member.remove_roles(mrole)

    @ban.error
    async def be(self, ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("you didn't mention anyone.")

    @commands.command() #Command aliases
    @commands.has_permissions(ban_members = True) #Check the message sender's permissions
    async def unban(self, ctx, member : discord.Member): #Function label and callbacks.

    #Roles 
        mrole = discord.utils.get(ctx.guild.roles, name="Banished")
        role = discord.utils.get(ctx.guild.roles, name="Cutie")
        channel = discord.utils.get(ctx.guild.channels, name="logs")
        operator = ctx.message.author

    #Function
        await ctx.channel.send(f"☁️ | successfully unbanned {member.mention}.", delete_after=4)
        await channel.send(f"☁️ | {operator.mention} successfully unbanned {member.mention}.")
        await member.add_roles(role)
        await time.sleep(1)
        await member.remove_roles(mrole)

    @unban.error #Error handler
    async def ube(self, ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("you didn't mention anyone.")

    @commands.command()
    @commands.has_permissions(kick_members = True) #Check the message sender's permissions
    async def kick(self, ctx,member : discord.Member,*,reason= "No reason provided."): #Delete the command message
        channel = discord.utils.get(ctx.guild.channels, name="Logs")
        operator = ctx.message.author
        await ctx.channel.send(f"🌩 | successfully kicked {member.mention}.", delete_after=4)
        await channel.send(f"🌩 | {operator.mention} successfully kicked {member.mention}.")
        await member.send("🌩 | you've been kicked from suki's apartment.")
        await member.kick(reason=reason)

    @kick.error
    async def ke(self, ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("you didn't mention anyone.")

    @commands.command(aliases=['del', 'clear', 'remove']) #Command aliases
    @commands.has_permissions(manage_messages = True) #Check the message sender's permissions
    async def delete(self, ctx,amount=2):
        if amount > 25:
            await ctx.channel.send("sorry you can only remove 25 messages at a time!", delete_after=4)
        else:
            await ctx.channel.purge(limit = amount + 1)
            await ctx.channel.send("complete!", delete_after=4)

def setup(client):
    client.add_cog(Moderation(client))
