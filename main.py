import os
import discord
from discord.ext import commands

from settings import *

from cogs import *

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')
GUILD_ID = os.getenv('GUILD_ID')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class ClientBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/',
                         intents=intents,
                         help_command=None)
        self.last_time = {}

    async def on_ready(self):

        await bot.tree.sync()

        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

        i = discord.utils.find(lambda s: s.name == SERVER, self.guilds)

        print(
            f'{self.user} has connected to Discord. \n'
            f'Connected to {i.name}(id: {i.id})'
        )

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and filename != '__init__.py':
                await self.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    bot = ClientBot()
    bot.run(TOKEN)