from discord.ext import commands
from discord import app_commands
import discord
import asyncio

class Administrator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="assign_role", description="Assign user(s) a server role")
    @app_commands.checks.bot_has_permissions(administrator=True)
    async def assign_role(self, interaction: discord.Interaction, role_name: str, user: str = None):
        role = discord.utils.get(interaction.guild.roles, name=role_name)

        if role is None:
            await interaction.response.send_message(f"Role {role_name} does not exist.", ephemeral=True)
            return
        
        if user is None or '':

            members_count = 0

            for member in interaction.guild.members:
                print(member)
                if role not in member.roles:
                    try:
                        await member.add_roles(role)
                        members_count += 1
                    except discord.Forbidden:
                        await interaction.followup.send("Could not assign role. Missing permission.", ephemeral=True)

            await interaction.response.send_message(f"Assigned role: {role}")

        else:
           
           member = discord.utils.find(lambda m: m.name.lower() == user.lower(), interaction.guild.members)

           if member:
                if role not in member.roles:
                    try:
                        await member.add_roles(role)
                    except discord.Forbidden:
                        await interaction.followup.send("Could not assign role. Missing permission.", ephemeral=True)

        await interaction.response.send_message(f"Assigned role: {role}")

        

async def setup(bot: commands.Bot):
    await bot.add_cog(Administrator(bot))