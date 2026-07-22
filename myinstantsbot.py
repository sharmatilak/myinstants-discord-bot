import os
import io
import re
import aiohttp
import uuid
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from typing import Optional
from myinstants import search_instants

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
        for cmd in synced:
            print(cmd.name, cmd.options)
    except Exception as e:
        print(e)


# Autocomplete

instant_cache = {}

async def instant_autocomplete(
    interaction: discord.Interaction,
    current: str,

):
    print("Autocomplete: ", current)
    if not current:
        return []

    try:
        results = await search_instants(current)
        print(results)
    except Exception:
        return []
    
    user_id = interaction.user.id

    # Create/clear this user's cache only
    instant_cache[user_id] = {}

    choices = []

    for result in results[:25]:
        key = uuid.uuid4().hex[:8] # Create a unique userid for each user

        instant_cache[user_id][key] = {
            "title": result["text"],
            "url": result["url"],
        }

        choices.append(
            app_commands.Choice(
                name=result["text"][:100],
                value=key
            )
        )

    return choices

