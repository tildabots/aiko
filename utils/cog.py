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
        key = await self.bot.kv.get(id)
        return key
