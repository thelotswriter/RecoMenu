import discord
from discord.ext import commands

from recomenu_functions import generate_menu


class Menu(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Generate a menu from your recipe book')
    async def menu(self, context, *, message=None):
        user = context.author
        uid = user.id
        generate_menu('user')


def setup(client):
    client.add_cog(Menu(client))
