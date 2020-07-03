import os
from resources import client

discord_bot_token = os.getenv('DD_DISCORD_BOTTOKEN', default=None)

if discord_bot_token is None:
    print("No Discord bot token found!")
    exit(1)
else:
    client.run(discord_bot_token)
