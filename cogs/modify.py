import discord
from discord.ext import commands
import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(path, 'functions')
sys.path.insert(0, path)

from modify_func import modify_recipe


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
