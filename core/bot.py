from discord.ext import commands
from utils.prefix import get_prefix
from core.config import Config
from logbook import Logger, StreamHandler
import sys
import discord
from osuapi import OsuApi, AHConnector


class Aiko(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config('config.yaml').config
        StreamHandler(sys.stdout).push_application()
        self.log = Logger('Aiko')
        self.osuapi = OsuApi(self.config['osuapi'], connector=AHConnector())

    async def on_ready(self):
        self.log.info(f'Aiko is ready! {len(self.guilds)} servers')
        await self.change_presence(activity=discord.Streaming(
            name=f'osu! // {get_prefix(self.config)}help',
            url='https://twitch.tv/monstercat'))

    async def on_message(self, message):
        if message.author.bot:
            return
        ctx = await self.get_context(message)
        await self.invoke(ctx)
