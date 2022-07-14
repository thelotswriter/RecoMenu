import discord
from discord.ext import commands
import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(path, 'functions')
sys.path.insert(0, path)

from delete_func import delete_recipe


class Delete(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Remove a recipe (automatically removes from all recipe books)')
    async def delete(self, context, *, message=None):
        user = context.author
        uid = user.id
        delete_recipe('name')


def setup(client):
    client.add_cog(Delete(client))
