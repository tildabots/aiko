def get_prefix(config):
    if config["prefix"]:
        return config["prefix"]
    else:
        return "^"  # default
