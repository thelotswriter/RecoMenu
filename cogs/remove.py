import discord
from discord.ext import commands
import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(path, 'functions')
sys.path.insert(0, path)

from remove_func import remove_recipe


class Remove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='remove a recipe from your recipe book')
    async def remove(self, context, *, message=None):
        user = context.author
        uid = user.id
        remove_recipe('user', 'name')


def setup(client):
    client.add_cog(Remove(client))
