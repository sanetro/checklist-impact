# Scrap api from https://api.genshin.dev/
import requests as re
import json 

artifacts = re.get("https://api.genshin.dev/artifacts")
artifactsResult = artifacts.json()


file = open("scrapper-api/artifacts.json", 'w')
file.write(str(artifactsResult))


