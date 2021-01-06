# project1-np575

09/22/2020 first milestone of Project-1 for getting twitter API working.
09/29/2020 second milestone of project-2 for getting the spoonacular API working.

This repository demostrates the use of Twitter API, spoonacular API (food) using Flask,HTML,CSS on AWS Cloud9.This repository consists of .pyfile written in python and flask,gitignore to hide the Twitter and spoonacular API keys, two folder for HTML and CSS, Procfie, requirements.txt and this Readme. The final version of the app is deployed on Heroku which can be found by clicking here: https://thawing-chamber-85195.herokuapp.com/

prerequisite: Flask, Python, HTML/CSS, basic knowledge of API.  

To use this repository and deploy the app, you must follow these steps:

0. Sign up for the twitter developer account: https://developer.twitter.com/en/apply-for-access.

1. Once you log-in to the account, navigate to https://developer.twitter.com/en/portal/projects-and-apps, create a
new project and identify API keys and tokens to use for the project.

2. Once you have the twitter API working, sign up for the Spoonacular API key by navigating to the https://spoonacular.com/food-api/console .

3. log in to your account and go to https://spoonacular.com/food-api/console#Profile and find your API keys.

4.clone this repo using command: git clone https://github.com/NJIT-CS490/project1-np575.git

5.create a copy of this repo in your local driectory environment.

6. After cloning the repo, install necessary softwares in your environment for the program to run:
Tweepy: pip install tweepy | sudo pip install tweepy | pip3 install tweepy | sudo pip3 install tweepy
Flask: pip install flask | sudo pip install flask | pip3 install flask | sudo pip3 install flask
run this command to check if it is installed: flask --version
Python-dotenv: pip install python-dotenv | sudo pip install python-dotenv | pip3 install python-dotenv | sudo pip3 install python-dotenv

7.create a .env file in the root directory and replace the keys with your credentials just like tweepy.env.
replace all 4 keys and tokens.(this repo has all the API keys stored in the tweepy.env file. tweet.py file is getting all the keys through the environment variables)

8. create a .env file in the root directory and replace the keys with your credentials just like spoonacular.env.

9. source both of these files first for example, source tweepy.env and spoonacular.env.

10. run the (python recipe.py) python file using whichever enviroment preffered. in cloud9, preview tab shows the live server with HTML/CSS.

11. push the command into the git and follow the next steps to deploy the app on heroku.

12. Sign up for heroku at heroku.com |  Install heroku by running npm install -g heroku.

13. Go through the following steps:
    heroku login -i
    heroku create (this will give you the heroku app link)
    git push heroku master
    
14. Navigate to your newly-created heroku site!

15. Add your secret keys (from step 2 and 3) by going to https://dashboard.heroku.com/apps
    and clicking into your app. Click on Settings, then scroll to "Config Vars." Click
    "Reveal Config Vars" and add the key value pairs for each variable in user_tweets.py
    Your config var key names should be:
    KEY=
    KEY_SECRET=
    TOKEN=
    TOKEN_SECRET=
    SPOONACULAR_KEY=
 
 16. Configure requirements.txt with all requirements needed to run your app.
 
 17. Configure Procfile with the command needed to run your app.
 
 18.If you are still having issues, you may use heroku logs --tail to see what's wrong.
 

Technical issues listed:
1. During the project, i did had trouble with the converting my python code to the flask and receieved importerror in .py file refer to this link
https://stackoverflow.com/questions/26075001/error-with-tweepy-oauthhandler and realzied my import wasn't initialized properly.
2. After grabbing the content i was stuck at Getting the datetime and url involved in the tweet content. later find out that in pythonwe can check
the propertties of the object by  print("\n".join(list(example.__dict__.keys()))) and that way got the detail for my API content and accessed the 
other details for the tweet content.
3. When i was at the stage to capture the url for image my content detail was in the API values but i wasn't getting the full image path so i had to debugg the code and then 
i finally solved the issue by string concatenation and got the url working.
4. To fetch the ingerdeints, I had to use another url to get the deatils. after debugging the API content, i had to create a loop to go over that key in the dictionary,
and then under the 'original' key i captured all of my content for the recipe.
5. while deplyoing the code. my heroku app wasn't reflecting the change i made after using heroku logs --tail , i found out that my twitter API wasn't working then i checked my config vars and realized that one my key had extra "," in the end of an key. After fixing that the ao started working back again.


Known issues:
1. Currently my program is fetching the tweetes through one randomly selected element in the list.But when we run the app it's fetching tweets with each Get request in the preview application of flask in cloud9 and in some of the cases it displays same tweet which can be improved by rethinking the list.
2. While my program runs on the flask python site, there could be the better option on hadling the empty response for the application. after debuging, i realized that the py can handle that condition but the falsk couldn't so which can be improved.
3. Right now we have the flask render template function, but we have so many variables to pass into that function in order for html to display py variables. i think that there could be an better way to handle this in flask given that this was my first experience in jinja2 templates. 

