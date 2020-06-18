from resources import client
from discord import Activity, Status, ActivityType


@client.event
async def on_ready():
    print("Eingeloggt als User {0.user}".format(client))
    print(client.guilds)
    atv = Activity(
        name="Bearbeitet Bewerbungen",
        type=ActivityType.playing,
        state="In Game (State)",
        detauls="In Game (Details)"
        )
    await client.change_presence(
        activity=atv,
        status=Status.online,
        afk=False
        )
