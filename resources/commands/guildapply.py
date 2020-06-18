import re
from discord import message
from discord import Embed
from resources import data
from resources import client
from resources.commands import success_and_delete, error_and_delete


async def invoke(message):
    msg = message.content.split()
    regex = r"^(https:\/\/sky\.lea\.moe\/stats\/)([\w\-\.\:\,\%\&]+)(\/)([\w\-\.\:\,\%\&]+)(\/{0,1})$"
    if not re.match(regex, msg[1]):
        await error_and_delete(message)
    else:
        embed = Embed(
            title="Gildenbewerbung von " + str(message.author),
            color=0xefaf21)
        embed.add_field(
            name="Profile URL",
            value=msg[1],
            inline=True)
        if len(msg) > 2:
            embed.add_field(
                name="Benutzerdefinierte Nachricht",
                value=' '.join(msg[2:]),
                inline=False)
        await client.guilds[0].get_channel(data['mod_channel']).send(
            embed=embed)
        await success_and_delete(message)
