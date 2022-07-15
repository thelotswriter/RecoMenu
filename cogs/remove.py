import discord
from discord.ext import commands

from recomenu_functions import remove_recipe


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
