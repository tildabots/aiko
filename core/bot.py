from discord.ext import commands
from utils.prefix import get_prefix
from utils.config import Config
from logbook import Logger, StreamHandler
import sys
import discord


class Mizaki(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config('config.yaml').config
        StreamHandler(sys.stdout).push_application()
        self.log = Logger('Mizaki')

    async def on_ready(self):
        self.log.info(f'Mizaki is ready! {len(self.bot.guilds)} servers')
        await self.bot.change_presence(activity=discord.Streaming(
            name=f'osu! // {get_prefix(self.config)}help',
            url='https://twitch.tv/monstercat'))

    async def on_message(self, message):
        if message.author.bot:
            return
        ctx = await self.get_context(message)
        await self.invoke(ctx)
