import discord
from discord.ext import commands
import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(path, 'functions')
sys.path.insert(0, path)

from random_func import random_recipe


class Random(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Display a random recipe')
    async def random(self, context, *, message=None):
        user = context.author
        uid = user.id
        random_recipe()


def setup(client):
    client.add_cog(Random(client))
