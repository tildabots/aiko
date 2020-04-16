from discord.ext import commands
from utils.cog import Cog
import discord
from osuapi.enums import OsuMode


class Profile(Cog):
    def __init__(self, bot):
        # everything's taken care of here
        super().__init__(bot)

    @commands.command()
    async def osu(self, ctx, user: discord.Member, mode: OsuMode = 0):
        print(dir(self))
        key = await self.bot.kv.get(user.id)
        if key is None:
            return await ctx.send(
                "I do not have you in the database."
                + f' Use `{self.bot.config["prefix"]}profile`'
                + " to begin setup."
            )


def setup(bot):
    bot.add_cog(Profile(bot))
