from discord.ext import commands
from utils.cog import Cog
import discord
from osuapi.enums import OsuMode


class Profile(Cog):
    def __init__(self, bot):
        # everything's taken care of here
        pass

    @commands.command()
    async def profile(self, ctx, user: discord.Member or str,
                      mode: OsuMode = 0):
        pass


def setup(bot):
    bot.add_cog(Profile(bot))
