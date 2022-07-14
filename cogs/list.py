import discord
from discord.ext import commands
import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(path, 'functions')
sys.path.insert(0, path)

from list_func import list_recipes


class List(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='List recipes (add a letter to limit the contents)')
    async def list(self, context, *, message=None):
        user = context.author
        uid = user.id
        list_recipes(arguments)


def setup(client):
    client.add_cog(List(client))
