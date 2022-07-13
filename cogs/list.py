import discord
from discord.ext import commands


class List(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='List recipes (add a letter to limit the contents)')
    async def list(self, context, *, message=None):
        user = context.author
        uid = user.id


def setup(client):
    client.add_cog(List(client))
