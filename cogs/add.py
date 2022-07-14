import discord
from discord.ext import commands
import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(path, 'functions')
sys.path.insert(0, path)

from add_func import add_recipe


class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Add a new recipe (automatically recorded to your recipe book)')
    async def add(self, context, *, message=None):
        user = context.author
        uid = user.id
        print('Hello add!')
        add_recipe('name', 'recipe', 'keywords', 'owner')


def setup(client):
    client.add_cog(Add(client))
