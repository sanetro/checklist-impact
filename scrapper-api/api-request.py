# Scrap api from https://api.genshin.dev/
import requests as re
import json 

artifacts = re.get("https://api.genshin.dev/artifacts")
artifactsResult = artifacts.json()
with open("scrapper-api/artifacts.json", "w") as file:
    json.dump(artifactsResult, file)

weapons = re.get("https://api.genshin.dev/weapons")
weaponsResult = weapons.json()
with open("scrapper-api/weapons.json", "w") as file:
    json.dump(weaponsResult, file)

characters = re.get("https://api.genshin.dev/characters")
charactersResult = characters.json()
with open("scrapper-api/characters.json", "w") as file:
    json.dump(charactersResult, file)

materialsTalentBook = re.get("https://api.genshin.dev/materials/talent-book")
materialsTalentBookResult = materialsTalentBook.json()
with open("scrapper-api/materialsTalentBook.json", "w") as file:
    json.dump(materialsTalentBookResult, file)

bossMaterial = re.get("https://api.genshin.dev/materials/boss-material")
bossMaterialResult = bossMaterial.json()
with open("scrapper-api/bossMaterial.json", "w") as file:
    json.dump(bossMaterialResult, file)

characterAscension = re.get("https://api.genshin.dev/materials/character-ascension")
characterAscensionResult = characterAscension.json()
with open("scrapper-api/characterAscension.json", "w") as file:
    json.dump(characterAscensionResult, file)

commonAscension = re.get("https://api.genshin.dev/materials/common-ascension")
commonAscensionResult = commonAscension.json()
with open("scrapper-api/commonAscension.json", "w") as file:
    json.dump(commonAscensionResult, file)







