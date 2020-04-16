from discord.ext import commands


class Cog(commands.Cog):
    """
    Simple extension of discord.ext.commands.Cog.

    Parameters:
    bot - Instance of the bot
    """

    def __init__(self, bot):
        self.bot = bot
