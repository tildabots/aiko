from discord.ext import commands
from utils.cog import Cog
import discord
from osuapi.enums import OsuMode


class Stats(Cog):
    def __init__(self, bot):
        # everything's taken care of here
        super().__init__(bot)

    # we bringing this shitcode back? hell yeah baby
    @classmethod
    def osu_mode_converter(self, mode=None):
        if mode == 0 or "standard" or "osu!standard" or "osu!" or None:
            return OsuMode.osu
        elif mode == 1 or "ctb" or "catchthebeat" or "osu!catch" or "catch":
            return OsuMode.catch
        elif mode == 2 or "taiko" or "osu!taiko":
            return OsuMode.taiko
        elif mode == 3 or "mania" or "osu!mania":
            return OsuMode.mania
        else:
            return None

    @commands.command()
    async def osu(self, ctx, user: discord.Member or str, mode: str or int = 0):
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
            else:
                profile = await self.bot.osuapi.get_user(
                    int(key["osu"]), mode=self.osu_mode_converter(mode)
                )
                await ctx.send(profile)


def setup(bot):
    bot.add_cog(Stats(bot))
