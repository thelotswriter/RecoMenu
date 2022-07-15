import discord
from discord.ext import commands

from recomenu_functions import recommend_recipe


class Recommend(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Recommend a recipe from your recipe book')
    async def recommend(self, context, *, message=None):
        user = context.author
        uid = user.id
        recommend_recipe('user')


def setup(client):
    client.add_cog(Recommend(client))
