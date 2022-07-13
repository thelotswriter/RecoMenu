import discord
from discord.ext import commands


class Random(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Display a random recipe')
    async def random(self, context, *, message=None):
        user = context.author
        uid = user.id


def setup(client):
    client.add_cog(random(client))
