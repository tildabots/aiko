def get_prefix(config):
    """
    Returns the prefix for the bot.

    Parameters:
    config - A dict that contains relevant config info.
    """
    if config["prefix"]:
        return config["prefix"]
    else:
        return "^"  # default
