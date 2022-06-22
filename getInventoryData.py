import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import requests as api
import json

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

url_base = 'https://www.bungie.net/Platform/Destiny2/'

linked_profiles = url_base + '254/Profile/18884453/LinkedProfiles/'
payload = {}
headers = {
    'x-api-key': os.environ['API_TOKEN']
}

get_linked = api.request("GET", linked_profiles, headers=headers, data=payload)
raw = get_linked.json()
membership_id = raw["Response"]["profiles"][0]["membershipId"]

name = raw["Response"]["bnetMembership"]["supplementalDisplayName"]
print('Accessing characters for ' + name + '...')

profile = url_base + '3/Profile/' + membership_id + '/?components=205'

get_profile = api.request("GET", profile, headers=headers, data=payload)
raw = get_profile.json()
data = raw["Response"]["characterEquipment"]["data"]
character_ids = list(data.keys())

char1data = data[character_ids[0]]["items"]
HunterItemIDs = []
for item in char1data:
    HunterItemIDs.append(item["itemHash"])

char2data = data[character_ids[1]]["items"]
TitanItemIDs = []
for item in char2data:
    TitanItemIDs.append(item["itemHash"])

char3data = data[character_ids[2]]["items"]
WarlockItemIDs = []
for item in char3data:
    WarlockItemIDs.append(item["itemHash"])

HunterGear = []
TitanGear = []
WarlockGear = []
for id in HunterItemIDs:
    entity_data = url_base + '/Manifest/DestinyInventoryItemDefinition/' + str(id)
    get_entity = api.request("GET", entity_data, headers=headers, data=payload)
    raw = get_entity.json()
    entity_name = raw["Response"]["displayProperties"]["name"]
    if(entity_name == 'Finishers' or entity_name == 'Emotes' or entity_name == 'Clan Banner'):
        pass;
    else:
        HunterGear.append(entity_name)
Hunter_Printed = {'Subclass': HunterGear[11], 'Kinetic': HunterGear[0], 'Energy': HunterGear[1], 'Power': HunterGear[2], 'Helmet': HunterGear[3], 'Arms': HunterGear[4], 'Chest': HunterGear[5], 'Legs': HunterGear[6], 'Class Item': HunterGear[7], 'Ghost': HunterGear[8], 'Sparrow': HunterGear[9], 'Ship': HunterGear[10], 'Emblem': HunterGear[12], 'Artifact': HunterGear[13]}

for id in TitanItemIDs:
    entity_data = url_base + '/Manifest/DestinyInventoryItemDefinition/' + str(id)
    get_entity = api.request("GET", entity_data, headers=headers, data=payload)
    raw = get_entity.json()
    entity_name = raw["Response"]["displayProperties"]["name"]
    if(entity_name == 'Finishers' or entity_name == 'Emotes' or entity_name == 'Clan Banner'):
        pass;
    else:
        TitanGear.append(entity_name)
Titan_Printed = {'Subclass': TitanGear[11], 'Kinetic': TitanGear[0], 'Energy': TitanGear[1], 'Power': TitanGear[2], 'Helmet': TitanGear[3], 'Arms': TitanGear[4], 'Chest': TitanGear[5], 'Legs': TitanGear[6], 'Class Item': TitanGear[7], 'Ghost': TitanGear[8], 'Sparrow': TitanGear[9], 'Ship': TitanGear[10], 'Emblem': TitanGear[12], 'Artifact': TitanGear[13]}
    
for id in WarlockItemIDs:
    entity_data = url_base + '/Manifest/DestinyInventoryItemDefinition/' + str(id)
    get_entity = api.request("GET", entity_data, headers=headers, data=payload)
    raw = get_entity.json()
    entity_name = raw["Response"]["displayProperties"]["name"]
    if(entity_name == 'Finishers' or entity_name == 'Emotes' or entity_name == 'Clan Banner'):
        pass;
    else:
        WarlockGear.append(entity_name)
Warlock_Printed = {'Subclass': WarlockGear[11], 'Kinetic': WarlockGear[0], 'Energy': WarlockGear[1], 'Power': WarlockGear[2], 'Helmet': WarlockGear[3], 'Arms': WarlockGear[4], 'Chest': WarlockGear[5], 'Legs': WarlockGear[6], 'Class Item': WarlockGear[7], 'Ghost': WarlockGear[8], 'Sparrow': WarlockGear[9], 'Ship': WarlockGear[10], 'Emblem': WarlockGear[12], 'Artifact': WarlockGear[13]}


print("Your Hunter has the following equipment...")
for key,value in Hunter_Printed.items():
    print(key + " ==> " + value)
print(" ")

print("Your Titan has the following equipment...")
for key,value in Titan_Printed.items():
    print(key + " ==> " + value)
print(" ")

print("Your Warlock has the following equipment...")
for key,value in Warlock_Printed.items():
    print(key + " ==> " + value)
