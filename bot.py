from discord.ext import commands
from core.bot import Aiko
from core.config import Config
import os

config = Config("config.yaml").config
help_command = commands.help.DefaultHelpCommand(dm_help=None)
bot = Aiko(
    command_prefix=commands.when_mentioned_or(config["prefix"]),
    description="osu! focused bot",
    help_command=help_command,
)


if __name__ == "__main__":
    for blahblah, blahblahblah, exts in os.walk("ext"):
        for ext in exts:
            if ext.endswith(".py"):
                try:
                    ext = ext.replace(".py", "")
                    bot.log.info(f"attempting to load {ext}")
                    bot.load_extension(f"ext.{ext}")
                except Exception:
                    bot.log.error(f"failed to load {ext}", exc_info=True)
                else:
                    bot.log.info(f"successfully loaded {ext}")
    bot.log.info("loading jishaku")
    bot.load_extension("jishaku")

bot.run(config["token"])
