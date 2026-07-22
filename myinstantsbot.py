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