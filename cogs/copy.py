import discord
from discord.ext import commands


class Copy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Add an existing recipe to your recipe book')
    async def copy(self, context, *, message=None):
        user = context.author
        uid = user.id


def setup(client):
    client.add_cog(Copy(client))
