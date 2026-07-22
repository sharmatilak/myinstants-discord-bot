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
        # print(results)
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


# Download Audio Bytes

async def download_file(url: str) -> bytes:

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            response.raise_for_status()  # Raises an exception for HTTP errors
            return await response.read()


# Slash Command

@bot.tree.command(
    name="instants",
    description="Search sounds"
)
@app_commands.allowed_installs(
    guilds=True,
    users=True,
)
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True,
)
async def instant(
    interaction: discord.Interaction,
    sound: str,
    message: Optional[str] = None
):
    user_cache = instant_cache.get(interaction.user.id)

    if user_cache is None:
        await interaction.response.send_message(
            "Your search expired. Please search again.",
            ephemeral=True,
        )
        return

    data = user_cache.get(sound)

    if data is None:
        await interaction.response.send_message(
            "That option is no longer valid. Please search again.",
            ephemeral=True,
        )
        return

    title = data["title"]
    safe_title = re.sub(r'[<>:"/\\|?*]', "_", title)
    url = data["url"]

    await interaction.response.defer()

    audio_data = await download_file(url)

    file = discord.File(
        io.BytesIO(audio_data),
        filename=f"{safe_title}.mp3"
    )

    if message is not None:
        await interaction.followup.send(
            content=message,
            file=file,
        )
    else:
        await interaction.followup.send(file=file)


    # Optional: clean up this user's cache after use
    instant_cache.pop(interaction.user.id, None)

bot.run(TOKEN)