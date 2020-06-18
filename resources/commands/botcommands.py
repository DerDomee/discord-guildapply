import os
from discord import message
from discord import Embed
from resources import client
from resources.commands import success_and_delete, error_and_delete


async def return_info(message):
    embed = Embed(
        title="Botinformation: Gildenbewerbungen",
        description="Bot zum Bewerben für die Streamgilde",
        color=0xdfdfdf)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/722892642450538647/973bffde74992ccf589c24c9745855c5.png")
    embed.add_field(
        name="Author",
        value="<@285720078031388673>",
        inline=True)
    embed.add_field(
        name="Version",
        value=os.getenv('BOT_VERSION', "0.1.0"),
        inline=True)
    embed.add_field(
        name="GitHub",
        value="https://github.com/derdomee/discord-guildapply",
        inline=False)
    embed.add_field(
        name="Botprefix für Commands",
        value="<@!722892642450538647>",
        inline=True)
    embed.add_field(
        name="Bugreports",
        value="[Issue auf GitHub erstellen](https://github.com/DerDomee/discord-guildapply/issues/new) oder kontaktiere mich (<@285720078031388673>) auf Discord!",
        inline=False)
    await message.channel.send(embed=embed)


async def resolve(message):
    msgstack = message.content.split()
    if not msgstack[0] == "<@!" + str(client.user.id) + ">":
        return

    if len(msgstack) is 1:
        await return_info(message)
    if len(msgstack) > 1:
        if msgstack[1] == "info":
            await return_info(message)
