# Aiko KV

This file documents the Key-Value system used in the Aiko Discord bot.

# What's behind it?
A simple Redis setup.

# Format
Each key in Redis is a Discord user ID and values are stored as dicts.
```py
{
    "osu": int  # A osu! user ID
}