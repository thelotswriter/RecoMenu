import discord
from discord.ext import commands


class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Add a new recipe (automatically recorded to your recipe book)')
    async def add(self, context, *, message=None):
        user = context.author
        uid = user.id


def setup(client):
    client.add_cog(Add(client))
