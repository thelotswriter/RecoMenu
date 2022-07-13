import discord
from discord.ext import commands


class Display(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Display a recipe')
    async def display(self, context, *, message=None):
        user = context.author
        uid = user.id


def setup(client):
    client.add_cog(Display(client))
