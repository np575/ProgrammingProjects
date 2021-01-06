# pylint: disable=W0614
# pylint: disable=W0611
# pylint: disable=W0612
# pylint: disable=W0401
# pylint: disable=R1705
# pylint: disable=R0914
# pylint: disable=C0116
# pylint: disable=C0411
import tweepy
from tweepy import *
import os
import datetime
import flask
from os.path import join, dirname  # importing libraries
from dotenv import load_dotenv
from tweepy import Cursor
import random
from datetime import datetime, date, timedelta, time
import requests
import sys

app = flask.Flask(__name__)

consumer_key = os.environ["KEY"]
consumer_secret = os.environ["KEY_SECRET"]
access_token = os.environ["TOKEN"]  # getting enviornment keysfor twitter api
access_token_secret = os.environ["TOKEN_SECRET"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(
    access_token, access_token_secret
)  # connecting api through tweepy
api = tweepy.API(auth)

dotenv_path = join(dirname(__file__), "spoonacular.env")
load_dotenv(dotenv_path)
spoonacular_key = os.environ["SPOONACULAR_KEY"]


@app.route("/")
def index():

    food_list = [
        "paneer",
        "ice cream",
        "pasta",
        "taco",
        "enchiladas",
        "pork",
        "chicken",
        "beef",
        "rice",
        "lamb",
        "samosa",
        "kebabs",
        "Malai Kofta",
        "pig",
    ]
    search_words = random.choice(food_list)
    date_since = "2020-09-02"
    # choosing the date since most of data from twitter api comes from past 3 weeks.

    url = (
        "https://api.spoonacular.com/recipes/search?query="
        + search_words
        + "&number=1&apiKey={}".format(spoonacular_key)
    )

    # user = api.get_user(account)
    # screen_name = user.screen_name
    # description = user.description
    response = requests.get(url)
    # print(type(response))
    json_body = response.json()
    # print((json_body))

    tweets = Cursor(api.search, q=search_words, lang="en", since=date_since).items(
        1
    )  # using cursor tofetch details for api
    print(search_words)
    print(json_body["results"])
    # print(json_body['results'].length)
    response = []

    if json_body["results"] == []:
        empty_data = print("recipes not found with {}".format(search_words))
        empty_handler = str(search_words)
        return flask.render_template("response.html", empty_handler=empty_handler)

    else:
        title = json_body["results"][0]["title"]
        time = json_body["results"][0]["readyInMinutes"]
        servings = json_body["results"][0]["servings"]
        url = json_body["results"][0]["sourceUrl"]
        url_path = json_body["baseUri"]
        jpg_path = json_body["results"][0]["image"]
        img_path = url_path + "/" + jpg_path
        foodid = json_body["results"][0]["id"]
        # print(img_path)

        tweet_list = []
        tweet_time = []
        tweet_username = []
        tweet_name = []
        tweet_urls = []

        url1 = (
            "https://api.spoonacular.com/recipes/"
            + str(foodid)
            + "/information?includeNutrition=false&apiKey={}".format(spoonacular_key)
        )
        response1 = requests.get(url1)
        json_body1 = response1.json()
        # print("fsf")
        # print((json_body1))
        ingredeint_list = []

        data = json_body1["extendedIngredients"]
        for ingredients in data:
            ingredeint_list.append(ingredients["original"])

        for tweet in tweets:
            # print("\n".join(list(tweet.__dict__.keys())))
            # to check the data in the api
            tweet_list.append(tweet.text)
            tweet_time.append(tweet.created_at)
            tweet_username.append(tweet.user.screen_name)
            tweet_urls.append(tweet.source_url)

        if tweet_list == []:
            empty_data = print("recipes not found with {}".format(search_words))
            empty_handler = str(search_words)
            return flask.render_template("response.html", empty_handler=empty_handler)

        return flask.render_template(
            "index.html",
            search_words=search_words,
            tweet_list=tweet_list,
            tweet_time=tweet_time,  # routing the data to html site
            tweet_username=tweet_username,
            tweet_urls=tweet_urls,
            title=title,
            time=time,
            servings=servings,
            url=url,
            img_path=img_path,
            ingredeint_list=ingredeint_list,
            list2_len=len(ingredeint_list),
            list_len=len(tweet_list),
        )


app.run(
    port=int(os.getenv("PORT", 8080)),  # running it on local port 8080
    host=os.getenv("IP", "0.0.0.0"),
)
