import discord
from discord.ext import commands


class Remove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='remove a recipe from your recipe book')
    async def remove(self, context, *, message=None):
        user = context.author
        uid = user.id


def setup(client):
    client.add_cog(Remove(client))
