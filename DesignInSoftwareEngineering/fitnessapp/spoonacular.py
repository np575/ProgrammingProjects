# pylint: disable=C0116
# pylint: disable=C0411
# pylint: disable=C0303
"""spoonacular.py"""
import requests
import json
from os.path import join, dirname
from dotenv import load_dotenv
import os


DOTENV_PATH = join(dirname(__file__), "sql.env")
load_dotenv(DOTENV_PATH)

spoonacular_key = os.environ["SPOONACULAR_KEY"]


def mealplan(calorie):
    url1 = (
        "https://api.spoonacular.com/mealplanner/generate?timeFrame=day&targetCalories="
    )
    url2 = "&apiKey={}"
    url3 = url1 + str(calorie) + url2
    url = url3.format(spoonacular_key)

    response = requests.get(url)
    json_body = response.json()
    breakfast = json_body["meals"][0]["title"]
    lunch = json_body["meals"][1]["title"]
    dinner = json_body["meals"][2]["title"]
    nutrients = json_body["nutrients"]

    meal_plan = {
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,
        "nutrients": nutrients,
    }

    return meal_plan


def foodsearch(name, cal):
    url1 = "https://api.spoonacular.com/recipes/complexSearch?query="
    url2 = "&addRecipeNutrition=true&maxCalories="
    url3 = url1 + str(name) + url2 + str(cal) + "&apiKey={}"
    url = url3.format(spoonacular_key)

    response = requests.get(url)
    json_body = response.json()
    food_return = json_body["results"]
    food_detail = {}
    
    i=0
    for item in food_return:
        key = "title"
        if key in item:
            image = item["id"]
            imageURL1 = "https://spoonacular.com/recipeImages/" + str(image)
            imageURL = imageURL1 + "-312x150.jpg"
            food_detail[i] = [item["title"],item["readyInMinutes"],item["sourceUrl"],imageURL, int(item["nutrition"]["nutrients"][0]["amount"])]
            i = i+1
            
        
    return food_detail