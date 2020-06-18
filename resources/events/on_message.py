from resources import client
from resources import data
from resources import save_data
from discord import message
from discord import role
from resources.commands import guildapply
from resources.commands import admincommands


def _strip_start(text, prefix):
    if not text.startswith(prefix):
        return text
    return text[len(prefix):]


def _strip_end(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:-len(suffix)]


@client.event
async def on_message(message):

    msg = message.content
    mentionprefix = "<@!" + str(client.user.id) + ">"

    if data['init_stage'] is 0:
        if message.author.permissions_in(message.channel).administrator \
                and message.content == "<@!" + str(client.user.id) + "> init":
            data['init_stage'] = 1
            data['admin_channel'] = message.channel.id
            data['mod_channel'] = ""
            data['log_channel'] = ""
            data['user_channels'] = []
            save_data()
    elif msg.startswith(mentionprefix):
        msg = _strip_start(msg, mentionprefix).strip()
        if message.channel.id in data['user_channels']:
            await guildapply.invoke(message)
        elif message.channel.id == data['admin_channel']:
            await admincommands.resolve(message)

    elif message.channel.id in data['user_channels']:
        if not message.author.permissions_in(message.channel).administrator:
            await message.delete()
