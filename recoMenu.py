import os
from discord.ext import commands

import db_manager

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix=['<@!996525735130972290> ', '<@996525735130972290> '])


@client.event
async def on_ready():
    print(f"{client.user} is connected!")


# Load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# Load cogs
path = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(os.path.join(path, 'cogs')):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Load players, pets, and eggs from database
connection = db_manager.create_connection()
with connection:
    db_manager.create_tables(connection)

client.run(token)
