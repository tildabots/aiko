from discord.ext import commands
from utils.cog import Cog
import discord
from osuapi.enums import OsuMode


class Stats(Cog):
    def __init__(self, bot):
        # everything's taken care of here
        super().__init__(bot)

    @commands.command()
    async def osu(self, ctx, user: str or discord.Member = None, mode: OsuMode = 0):
        if type(user) == discord.Member:
            key = await self.lookup_user(user.id)
            if key is None:
                if user.id == ctx.message.author.id:
                    return await ctx.send(
                        "I do not have you in my database."
                        + f' Run {self.bot.config["prefix"]}config'
                        + " to configure your profile."
                    )
                else:
                    return await ctx.send(
                        "I could not find that user in my database."
                        + f' Tell them to run {self.bot.config["prefix"]}config'
                        + " to configure their profile."
                    )


def setup(bot):
    bot.add_cog(Stats(bot))
