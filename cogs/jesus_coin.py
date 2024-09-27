from discord.ext import commands
from discord import app_commands
import discord
import random
import asyncio

class JesusCoin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.checks.cooldown(1,2)
    @app_commands.command(name="jesuscoin", description="Ask the coin a question to decide your fate.")
    async def jesus_coin(self, interaction: discord.Interaction, question: str):


        
        choices = random.choice(["Yes", "No"])

        await interaction.response.send_message(f"**Question:** *{question}*")
        await asyncio.sleep(3)

        a1 = await interaction.followup.send("I will now flip the coin.")
        a2 = await interaction.followup.send("https://tenor.com/view/flipping-a-coin-parker-mccollum-tails-i-lose-song-heads-or-tails-coin-toss-gif-12106700906845833563")

        await asyncio.sleep(3)
        await a1.delete()
        await a2.delete()

        await interaction.followup.send(f"{interaction.user.mention} The answer is: **{choices}**")



async def setup(bot: commands.Bot):
    await bot.add_cog(JesusCoin(bot))
