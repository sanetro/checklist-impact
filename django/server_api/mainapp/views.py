from django.shortcuts import render
from django.http import JsonResponse
import requests as re
# Create your views here.

def showArtifacts(request):
    artifacts = re.get("https://api.genshin.dev/artifacts")
    artifactsResult = artifacts.json()
    res = {
        'success': True,
        'artifacts': artifactsResult
    }
    return JsonResponse(res)

def showWeapons(request):
    weapons = re.get("https://api.genshin.dev/weapons")
    weaponsResult = weapons.json()
    res = {
        'success': True,
        'artifacts': weaponsResult
    }
    return JsonResponse(res)

def showCharacters(request):
    characters = re.get("https://api.genshin.dev/characters")
    charactersResult = characters.json()
    res = {
        'success': True,
        'artifacts': charactersResult
    }
    return JsonResponse(res)

def showMaterialsTalentBook(request):
    materialsTalentBook = re.get("https://api.genshin.dev/materials/talent-book")
    materialsTalentBookResult = materialsTalentBook.json()
    res = {
        'success': True,
        'artifacts': materialsTalentBookResult
    }
    return JsonResponse(res)

def showBossMaterial(request):
    bossMaterial = re.get("https://api.genshin.dev/materials/boss-material")
    bossMaterialResult = bossMaterial.json()
    res = {
        'success': True,
        'artifacts': bossMaterialResult
    }
    return JsonResponse(res)

def showCharacterAscension(request):
    characterAscension = re.get("https://api.genshin.dev/materials/character-ascension")
    characterAscensionResult = characterAscension.json()
    res = {
        'success': True,
        'artifacts': characterAscensionResult
    }
    return JsonResponse(res)

def showCommonAscension(request):
    commonAscension = re.get("https://api.genshin.dev/materials/common-ascension")
    commonAscensionResult = commonAscension.json()
    res = {
        'success': True,
        'artifacts': commonAscensionResult
    }
    return JsonResponse(res)
