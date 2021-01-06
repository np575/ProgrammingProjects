import tweepy
from tweepy import *
import os
import datetime
import flask
from os.path import join, dirname           #importing libraries
from dotenv import load_dotenv
from tweepy import Cursor
import random
from datetime import datetime,date,timedelta,time

app = flask.Flask(__name__)

consumer_key = os.environ['KEY']
consumer_secret = os.environ['KEY_SECRET']
access_token = os.environ['TOKEN']                  #getting enviornment keysfor twitter api
access_token_secret = os.environ['TOKEN_SECRET']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)        # connecting api through tweepy
api = tweepy.API(auth)



@app.route('/')
def index():
    
    food_list=["pasta","pizza","ice cream","samosa","butter chicken","masala dosa","Neapolitan pizza","sushi","cheeseburger","fajitas","enchiladas"]
    search_words = random.choice(food_list)
    date_since = "2020-09-02"
    #choosing the date since most of data from twitter api comes from past 3 weeks.
    
    #user = api.get_user(account)
    #screen_name = user.screen_name
    #description = user.description
    
    tweets = Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(1)    #using cursor tofetch details for api
    
    #print(tweets[screen_name])
   
    #if time == date_since:
    #    exit(0)

   
    tweet_list=[]
    tweet_time=[]
    tweet_username=[]
    tweet_name=[]
    tweet_urls=[]
    
    for tweet in tweets:
        
        #print("\n".join(list(tweet.__dict__.keys())))
        # to check the data in the api
        
        tweet_list.append(tweet.text)
        tweet_time.append(tweet.created_at)
        tweet_username.append(tweet.user.screen_name)
        tweet_urls.append(tweet.source_url)
        
        #print(type(tweet.text))
        #print(tweet.text)
    
    #username=tweet.user
       
    return flask.render_template(
        "index.html",
        search_words=search_words,
        tweet_list = tweet_list,
        tweet_time = tweet_time,            #routing the data to html site
        tweet_username=tweet_username,
        tweet_urls=tweet_urls,
        list_len = len(tweet_list)
       )
    
app.run(
    port = int(os.getenv("PORT", 8080)),   #running it on local port 8080
    host = os.getenv("IP", "0.0.0.0")
)