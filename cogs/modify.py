import discord
from discord.ext import commands


class Modify(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Modify a recipe')
    async def modify(self, context, *, message=None):
        user = context.author
        uid = user.id


def setup(client):
    client.add_cog(Modify(client))