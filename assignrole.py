import discord
from discord.ext import commands
from discord.ui import Button, View
import os

TOKEN = "MTMxNjQ2MDQ2NTY4MTA3NjI0NA.G9gtOW.wjMWAjUF7HSsOGCcy-WOUaqQzgrFPjtB2oRi8I"  # Replace with your bot's token
ROLE_ID = 1340431165609349181  # Replace with the actual role ID
CHANNEL_ID = 480643168996687874  # Replace with the channel ID where the embed should be sent

intents = discord.Intents.default()
intents.members = True  # Enable member intents

bot = commands.Bot(command_prefix="!", intents=intents)

class RoleButton(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="I Do 🚀", style=discord.ButtonStyle.green, custom_id="assign_role")
    async def assign_role(self, interaction: discord.Interaction, button: Button):
        guild = interaction.guild
        role = guild.get_role(ROLE_ID)
        member = interaction.user

        if role in member.roles:
            await interaction.response.send_message("🎉 You already have the role! Let's keep grinding.", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("✅ Role successfully assigned! Welcome to the creator community! 🎉", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="🚀 **I am diving into Viral Villa** to level up my creator game—no excuses, just pure grind! 🔥",
            description="Click **I Do** to become a Creator",
            color=discord.Color.green()
        )
        embed.set_footer(text="Let’s Fucking Go! 🔥")  # Add a footer for extra flair

        view = RoleButton()
        await channel.send(embed=embed, view=view)

bot.run(TOKEN)
