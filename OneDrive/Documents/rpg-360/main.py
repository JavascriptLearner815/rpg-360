import discord
from discord.ext import commands
import random

command_prefix = '$'
help_command = 'help'
description = 'My first Python (Discord.py) bot! Have fun!!!!! Inspired by RPG-3000 (RPG-3000 is made by zaneanderman).'
invite_link = '<https://discord.com/oauth2/authorize?client_id=805944957533159454&scope=bot&permissions=347200>'

intents = discord.Intents.default()
intents.members = True # Must also be enabled on dashboard
intents.presences = True # Must also be enabled on dashboard

bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


class Info(commands.Cog):
    """Commands that have additional content or tips/tricks"""

    def __init__(self):
        bot.help_command.cog = self

    @commands.command(description='Add RPG-360 to another server')
    async def invite(self, ctx):
        """Add RPG-360 to another server"""
        await ctx.send(invite_link)


bot.add_cog(Info())

with open("./token.txt", "r") as f:
    token = f.read()
    bot.run(str(token))
