import json
from discord import message
from discord import Embed
from datetime import datetime
from resources import data, save_data
from resources import client
from resources.commands import success_and_delete, error_and_delete


def _strip_start(text, prefix):
    if not text.startswith(prefix):
        return text
    return text[len(prefix):]


def _strip_end(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:-len(suffix)]


async def add_userchannel(message, msgstack):
    if len(msgstack) is not 1:
        await error_and_delete(message)
    elif msgstack[0].startswith("<#") and msgstack[0].endswith(">"):
        channelid = _strip_start(msgstack[0], "<#")
        channelid = _strip_end(channelid, ">")
        channelid = int(channelid)
        print(channelid)
        if client.guilds[0].get_channel(channelid) is not None and \
                channelid not in data['user_channels']:
            data['user_channels'].append(channelid)
            save_data()
            await success_and_delete(message)
        else:
            await error_and_delete(message)
    else:
        await error_and_delete(message)


async def remove_userchannel(message, msgstack):
    if len(msgstack) is not 1:
        await error_and_delete(message)
    elif msgstack[0].startswith("<#") and msgstack[0].endswith(">"):
        channelid = _strip_start(msgstack[0], "<#")
        channelid = _strip_end(channelid, ">")
        channelid = int(channelid)
        print(channelid)
        if channelid in data['user_channels']:
            data['user_channels'].remove(channelid)
            save_data()
            await success_and_delete(message)
        else:
            await error_and_delete(message)
    else:
        await error_and_delete(message)


async def add_genericbotchannel(message, msgstack):
    if len(msgstack) is not 1:
        await error_and_delete(message)
    elif msgstack[0].startswith("<#") and msgstack[0].endswith(">"):
        channelid = _strip_start(msgstack[0], "<#")
        channelid = _strip_end(channelid, ">")
        channelid = int(channelid)
        print(channelid)
        if client.guilds[0].get_channel(channelid) is not None and \
                channelid not in data['generic_bot_channels']:
            data['generic_bot_channels'].append(channelid)
            save_data()
            await success_and_delete(message)
        else:
            await error_and_delete(message)
    else:
        await error_and_delete(message)


async def remove_genericbotchannel(message, msgstack):
    if len(msgstack) is not 1:
        await error_and_delete(message)
    elif msgstack[0].startswith("<#") and msgstack[0].endswith(">"):
        channelid = _strip_start(msgstack[0], "<#")
        channelid = _strip_end(channelid, ">")
        channelid = int(channelid)
        print(channelid)
        if channelid in data['generic_bot_channels']:
            data['generic_bot_channels'].remove(channelid)
            save_data()
            await success_and_delete(message)
        else:
            await error_and_delete(message)
    else:
        await error_and_delete(message)


async def set_logchannel(message, msgstack):
    if len(msgstack) is not 1:
        await error_and_delete(message)
    elif msgstack[0].startswith("<#") and msgstack[0].endswith(">"):
        channelid = _strip_start(msgstack[0], "<#")
        channelid = _strip_end(channelid, ">")
        channelid = int(channelid)
        print(channelid)
        if client.guilds[0].get_channel(channelid) is not None:
            data['log_channel'] = channelid
            save_data()
            await success_and_delete(message)
        else:
            await error_and_delete(message)
    else:
        await error_and_delete(message)


async def set_modchannel(message, msgstack):
    if len(msgstack) is not 1:
        await error_and_delete(message)
    elif msgstack[0].startswith("<#") and msgstack[0].endswith(">"):
        channelid = _strip_start(msgstack[0], "<#")
        channelid = _strip_end(channelid, ">")
        channelid = int(channelid)
        print(channelid)
        if client.guilds[0].get_channel(channelid) is not None:
            data['mod_channel'] = channelid
            save_data()
            await success_and_delete(message)
        else:
            await error_and_delete(message)
    else:
        await error_and_delete(message)


async def set_adminchannel(message, msgstack):
    if len(msgstack) is not 1:
        await error_and_delete(message)
    elif msgstack[0].startswith("<#") and msgstack[0].endswith(">"):
        channelid = _strip_start(msgstack[0], "<#")
        channelid = _strip_end(channelid, ">")
        channelid = int(channelid)
        print(channelid)
        if client.guilds[0].get_channel(channelid) is not None:
            data['admin_channel'] = channelid
            save_data()
            await success_and_delete(message)
        else:
            await error_and_delete(message)
    else:
        await error_and_delete(message)


async def stop_bot(message, msgstack):
    embed = Embed(
        title="Gildenbewerbungen Bot fährt herunter",
        description="Adminbefehl hat Neustart oder Herunterfahren ausgelöst",
        color=0xef4141,
        timestamp=datetime.now())
    embed.set_footer(
        text="Ausgelöst durch " + str(message.author) + " ("
             + str(message.author.id) + ")")
    logchannel = client.guilds[0].get_channel(data['log_channel'])
    await logchannel.send(embed=embed)
    await success_and_delete(message)
    await client.logout()


async def resolve(message):
    msgstack = message.content.split()
    if msgstack[1] == "add_userchannel":
        await add_userchannel(message, msgstack[2:])
    elif msgstack[1] == "remove_userchannel":
        await remove_userchannel(message, msgstack[2:])
    elif msgstack[1] == "set_modchannel":
        await set_modchannel(message, msgstack[2:])
    elif msgstack[1] == "set_logchannel":
        await set_logchannel(message, msgstack[2:])
    elif msgstack[1] == "set_adminchannel":
        await set_adminchannel(message, msgstack[2:])
    elif msgstack[1] == "add_generic_botchannel":
        await add_genericbotchannel(message, msgstack[2:])
    elif msgstack[1] == "remove_generic_botchannel":
        await remove_genericbotchannel(message, msgstack[2:])
    elif msgstack[1] == "stop":
        await stop_bot(message, msgstack[2:])
