from discord.ext import commands
from utils.cog import Cog
import discord
from osuapi.enums import OsuMode


class Profile(Cog):
    def __init__(self, bot):
        # everything's taken care of here
        pass

    @commands.command()
    async def osu(self, ctx, user: discord.Member, mode: OsuMode = 0):
        async with ctx.bot.kv.get(user.id) as key:
            if key is None:
                return await ctx.send(
                    "I do not have you in the database."
                    + f' Use `{self.bot.config["prefix"]}profile`'
                    + " to begin setup."
                )


def setup(bot):
    bot.add_cog(Profile(bot))
