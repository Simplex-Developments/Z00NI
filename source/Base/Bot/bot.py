import nextcord
from nextcord.ext import commands
import os
from loguru import logger

from source.Base.Helper.keep_alive import keep_alive

from .init import __init__

def start(version):
    bot = commands.Bot(command_prefix="?", case_insensitive=True)

    keep_alive()

    @bot.event
    async def on_ready():
        logger.info(f"Eingeloggt als {bot.user} | {version}")
        await bot.change_presence(
        activity=nextcord.Activity(
            type=nextcord.ActivityType.watching,
            name=f"?help | {version}"),
            status=nextcord.Status.online)

    @bot.command(name="botinfo")
    async def botinfo(ctx):
        embed = nextcord.Embed(title="Bot-Informationen", description=f"Version: {version}", colour=nextcord.Colour.gold(), timestamp=ctx.message.created_at)
        return await  ctx.send(embed=embed)

    __init__(bot, version)

    bot.run(os.getenv("tokendev"))