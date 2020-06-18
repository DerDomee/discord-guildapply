import discord
import json

data = {}


def save_data():
    with open('config_data.json', 'w') as save_file:
        json.dump(data, save_file, indent=2)
    return


try:
    config_file = open('config_data.json')
except FileNotFoundError:
    data['init_stage'] = 0
    pass
else:
    data = json.load(config_file)
    config_file.close()
save_data()


client = discord.Client()

from resources import events
