#Version 1.0.2

import os
import discord
from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv
import datetime


load_dotenv()

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

        try:
            guild = discord.Object(id=594913076390789138)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as e:
            print(f"Error syncing commands: {e}")


intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix='!', intents=intents)

GUILD_ID = discord.Object(id=594913076390789138)

@client.tree.command(name='countdown', description='Countdown until release', guild=GUILD_ID)
async def countdown(interaction: discord.Interaction):
    now = datetime.datetime.now()
    release = datetime.datetime(2026, 1, 15, 12)
    await interaction.response.send_message(f'Hackero Next releases in {release - now}!!!')

client.run(os.getenv('DISCORD_TOKEN'))