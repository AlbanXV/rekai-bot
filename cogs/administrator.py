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
        """
        Assign roles for the user(s).

        If the user parameter is empty, the chosen role will be assigned to everyone.

        args: 
            - self
            - interaction: discord.Interaction
            - role_name: str
            - user: str [Opt]

        returns:
            - None
        
        """
        
        role = discord.utils.get(interaction.guild.roles, name=role_name)

        if role is None:
            await interaction.response.send_message(f"Role {role_name} does not exist.", ephemeral=True)
            return
        
        if user is None or '':

            members_count = 0
            # await interaction.response.defer()
            for member in interaction.guild.members:
                print(member)
                if role not in member.roles:
                    try:
                        await member.add_roles(role)
                        members_count += 1
                    except discord.Forbidden:
                        await interaction.followup.send("Could not assign role. Missing permission.", ephemeral=True)

            await interaction.response.send_message(f"Assigned role: {role} to everyone")

        else:
           
           member = discord.utils.find(lambda m: m.name.lower() == user.lower(), interaction.guild.members)

           if member:
                if role not in member.roles:
                    try:
                        await member.add_roles(role)
                    except discord.Forbidden:
                        await interaction.followup.send("Could not assign role. Missing permission.", ephemeral=True)

        await interaction.response.send_message(f"Assigned role: {role} to user {user}")


    @app_commands.command(name="unassign_role", description="Remove user(s) specific server role")
    @app_commands.checks.bot_has_permissions(administrator=True)
    async def unassign_role(self, interaction: discord.Interaction, role_name: str, user: str):
        """
        Remove role from a user.

        args: 
            - self
            - interaction: discord.Interaction
            - role_name: str
            - user: str

        returns:
            - None
        
        """
        role = discord.utils.get(interaction.guild.roles, name=role_name)

        if role is None:
            await interaction.response.send_message(f"Role {role_name} does not exist.", ephemeral=True)
            return

        member = discord.utils.find(lambda m: m.name.lower() == user.lower(), interaction.guild.members)
        print(member)
        if member:
            if role in member.roles:
                try:
                    await member.remove_roles(role)
                    print(f"removed role {role} from user {user}")
                    await interaction.response.send_message(f"Unassigned role: {role} from user {user}")
                except discord.Forbidden:
                    await interaction.followup.send("Could not assign role. Missing permission.", ephemeral=True)
        
        else:
            await interaction.response.send_message(f"User {user} does not exist.", ephemeral=True)
            return


    @app_commands.command(name="clear_messages", description="Delete specified amount of messages in a channel")
    @app_commands.checks.bot_has_permissions(administrator=True)
    async def clear_messages(self, interaction: discord.Interaction, amount: int):
        """
        Clear messages in a channel.

        Limit amount between 1-100 to delete messages.

        args: 
            - self
            - interaction: discord.Interaction
            - amount: int

        returns:
            - None
        
        """
        
        if amount == 0:
            await interaction.response.send_message("No amount was entered.")
            return

        if amount < 1 or amount > 100:
            await interaction.response.send_message("Amount has a limit between 1-100 to delete messages.")

        delete = await interaction.channel.purge(limit=amount)

        await interaction.response.send_message(f"Successfully deleted {amount} messages.")

async def setup(bot: commands.Bot):
    """
        Add the cog(s) / command(s) function to the bot

        args: 
            - bot: commands.Bot

        returns:
            - None
        
        """
    await bot.add_cog(Administrator(bot))