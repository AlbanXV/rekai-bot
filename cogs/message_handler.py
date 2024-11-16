import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from utility.words import words
from utility.users import *
from utility.user_timers import user_timers

RESPONSE_INTERVAL = 3600 # 1 time i sekunder

load_dotenv()
LOG = int(os.getenv('LOG_CHANNEL')) # channel-id

class MessageHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        A function that is called when a message is created and sent.
        No commands necessary.

        args: 
            - self
            - message: Any

        returns:
            - None
        
        """   

        if message.author == self.bot.user:
            return

        for i in words:
            if i in message.content.lower():
                await message.channel.send(f"{message.author.mention} said {i} 🤣🤣")
                return
            
            if message.author.id == xizzio:
                await user_timers(message=message, user_id=xizzio, response=f"guys, <@{xizzio}> is talking. https://tenor.com/view/open-door-slide-door-shocked-surprised-gif-17800135", interval=RESPONSE_INTERVAL, recent=self.last_time)
                return
            
            if message.author.id == asif:
                await user_timers(message=message, user_id=asif, response=f"<@{asif}> https://tenor.com/view/skeleton-mewing-mewing-meme-think-thinking-gif-8986451654826218658", interval=RESPONSE_INTERVAL, recent=self.last_time)
                return
            
            if "genshin" in message.content.lower():
                await message.channel.send("genshit*")

            await self.bot.process_commands(message)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        
        log_channel = self.bot.get_channel(LOG)

        if log_channel:

            embed = discord.Embed(title="Message Deleted",
                                description=f"Message by {message.author.mention} deleted",
                                color=discord.Color.red())
            embed.add_field(name="Message Content",
                            value=message.content or "No content available",
                            inline=False)
            embed.set_footer(text=f"Author ID: {message.author.id} | Message ID: {message.id}")

            await log_channel.send(embed=embed)
        else:
            print(f"Log channel not found. Deleted message: {message.content} from {message.author}")
        


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        log_channel = self.bot.get_channel(LOG)

        if log_channel:

            embed = discord.Embed(title="Message Edited",
                                description=f"Message by {before.author.mention} deleted",
                                color=discord.Color.orange())
            embed.add_field(name="Message Content [Before]",
                            value=before.content or "No content available",
                            inline=False)
            embed.add_field(name="Message Content [After]",
                            value=after.content or "No content available",
                            inline=False)
            embed.set_footer(text=f"Author ID: {before.author.id} | Message ID: {before.id}")

            await log_channel.send(embed=embed)
        else:
            print(f"Log channel not found. Edited message: {before.content} -> {after.content} from {before.author}")
        


async def setup(bot):
    """
        Add the cog(s) / command(s) function to the bot

        args: 
            - bot: commands.Bot

        returns:
            - None
        
    """
    await bot.add_cog(MessageHandler(bot))