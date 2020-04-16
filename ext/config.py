from utils.cog import Cog
from discord.errors import Forbidden
from discord.ext import commands


class Config(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command()
    async def setup(self, ctx):
        key = await self.lookup_user(ctx.message.author.id)
        if key is None:
            try:
                ctx.message.author.send("**Welcome to Aiko!**")
            except Forbidden:
                return await ctx.send(
                    "I was not able to send a DM to you."
                    + " Enable your DMs and try again."
                )
