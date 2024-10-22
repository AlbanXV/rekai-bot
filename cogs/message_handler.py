import discord
from discord.ext import commands

from utility.words import words
from utility.users import *
from utility.user_timers import user_timers

RESPONSE_INTERVAL = 3600 # 1 time i sekunder

class MessageHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

            if message.author == self.bot.user:
                return

            for i in words:
                if i in message.content.lower():
                    await message.channel.send(f"{message.author.mention} said {i} 🤣🤣")
                    return
            
            if message.author.id == xizzio:
                await user_timers(message=message, user_id=xizzio, response=f"guys, <@{xizzio}> is talking. https://tenor.com/view/open-door-slide-door-shocked-surprised-gif-17800135", interval=RESPONSE_INTERVAL)
                return
            
            if message.author.id == asif:
                await user_timers(message=message, user_id=asif, response=f"<@{asif}> https://tenor.com/view/skeleton-mewing-mewing-meme-think-thinking-gif-8986451654826218658", interval=RESPONSE_INTERVAL, recent=self.last_time)
                return
            
            if "genshin" in message.content.lower():
                await message.channel.send("genshit*")

            await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(MessageHandler(bot))