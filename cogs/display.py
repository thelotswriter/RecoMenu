import discord
from discord.ext import commands
import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(path, 'functions')
sys.path.insert(0, path)

from display_func import display_recipe


class Display(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Display a recipe')
    async def display(self, context, *, message=None):
        user = context.author
        uid = user.id
        display_recipe('name')


def setup(client):
    client.add_cog(Display(client))
