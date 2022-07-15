import discord
from discord.ext import commands

from recomenu_functions import modify_recipe

class Modify(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Modify a recipe')
    async def modify(self, context, *, message=None):
        user = context.author
        uid = user.id
        modify_recipe('name', 'recipe', 'keywords')


def setup(client):
    client.add_cog(Modify(client))
