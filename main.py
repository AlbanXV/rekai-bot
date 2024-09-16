import os

from settings import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
    #for i in client.guilds:
    #    if i.name == SERVER:
    #        break
    i = discord.utils.find(lambda s: s.name == SERVER, client.guilds)

    print(
        f'{client.user} has connected to Discord. \n'
        f'Connected to {i.name}(id: {i.id})'
    )

client.run(TOKEN)