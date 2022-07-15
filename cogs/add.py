import discord
from discord.ext import commands

from recomenu_functions import add_recipe


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
