from discord.ext import commands


class Cog(commands.Cog):
    """
    Simple extension of discord.ext.commands.Cog.

    Parameters:
    bot - Instance of the bot
    """

    def __init__(self, bot):
        self.bot = bot

    async def lookup_user(self, id: int):
        # Sidenote: why the fuck do I have to manually request UTF-8?
        # I thought this was 2020, and I don't know a single thing that actually
        # uses bytes. Also aioredis docs are absolute shit. End of rant.
        key = await self.bot.kv.hgetall(id, encoding="utf-8")
        return key
