# app.py
# pylint: disable=E1101
# pylint: disable=C0301
# pylint: disable=C0413
# pylint: disable=W0603
# pylint: disable=W0611
# pylint: disable=W0612
# pylint: disable=W1401
# pylint: disable=W1508
# pylint: disable=R1705
# pylint: disable=C0116
# pylint: disable=invalid-name
# pylint: disable=C0114


# app.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

import flask
import flask_sqlalchemy
import flask_socketio

from flask import request
import requests
import json
from datetime import datetime
import re


INPUT = "in"
BOT_PREFIX = "!!"
KEY_IS_BOT = "is_bot"
KEY_BOT_COMMAND = "bot_command"
KEY_MESSAGE = "message"

ADDRESSES_RECEIVED_CHANNEL = 'input received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

# sql_user = os.environ['SQL_USER']
# sql_pwd = os.environ['SQL_PASSWORD']
# dbuser = os.environ['USER']

database_uri = os.environ['DATABASE_URL']


# 'postgresql://{}:{}@localhost/postgres'.format(
   # sql_user, sql_pwd)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app


db.create_all()
db.session.commit()
import models

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")

def print_request_sid():
    #print(flask.request.sid)
    return flask.request.sid

def emit_all_addresses(channel):

    #print("TODO")
    all_addresses =[ \
        db_address.address for db_address in \
        db.session.query(models.Usps).all()]
    socketio.emit(channel,{
        'allAddresses': all_addresses
    })

def translate_call(string):
    url = "https://api.funtranslations.com/translate/pirate.json?text={}".format(string)
    response = requests.get(url)
    if response.status_code == 200:
        json_body = response.json()
        #print(json_body["contents"]["translated"])
        message=json_body["contents"]["translated"]
        #print(message)
        return "Jarvis(Bot)-> " + message
    else:
        return "No response from the server please try again later !"



user_count=[]
count_user=0
uname=[]

@socketio.on('connect')

def on_connect():
    #print('Someone connected!')
    user_count.append('connect')
    #print(ucount)
    global count_user #global statement
    count_user +=1
    #print(count)
    socketio.emit('connected', {
        'test': count_user
    })
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    return count_user
@socketio.on('disconnect')
def on_disconnect():
    #print ('Someone disconnected!')
    mystr='connect'
    global count_user
    count_user -=1
    #print(count)
    user_count.remove(mystr)
    socketio.emit('disconnected', {
        'test': count_user
    })
@socketio.on('new google user')
def on_new_google_user(data):
    #print("Got an event for new google user input with data:", data)

    #print(data['name']);
    #print(data['picture']);
    user_count.append('connect')
    socketio.emit('connected', {
        'test': count_user
    })
    # username=data['name']
    picture=data['picture']
    # socketio.emit('username', {
    #     'user_name': username
    # })
    socketio.emit('new google image',{
        'image': picture
    })
    db.session.add(models.Usps(data['name'] + ": "))
    db.session.commit()
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    google_user ={  'name': data['name'], 'picture': data['picture']}
    return google_user


@socketio.on('new address input')
def on_new_address(data):
    #print("Got an event for new address input with data:", data)
    message=""
    new_str=data["address"]
    checker=re.search("(?P<url>https?://[^\s]+)", new_str)
    None_check=None
    if checker == None_check:
        test_var="here"
        #print("Response form server: Not a url")
        #str_check="None"
    else:
        str_check=(re.findall(r'(https?://[^\s]+)', new_str))
    str_check=(re.findall(r'(https?://[^\s]+)', new_str))
    if new_str == "!! about":
        #print("here")
        message="Jarvis(Bot)-> I can translate text for you in pirate language.  write !! help  to see what commands I can take. " + dt_string
    elif new_str.startswith("!! help"):
        message="Jarvis(Bot)-> I can be used for any of these commands: !! about | !! help | !! translate | !! time " + dt_string
    elif new_str.startswith("!! translate"):
        st_data=data["address"]
        #print(st.find("e "))
        index1=(st_data.find("e ")+2)
        new_str1=st_data[index1: ]
        #print(new_str1)
        message=translate_call(new_str1)
        #print(message)
    elif new_str.startswith("!! time"):
        now1 = datetime.now()
        dt_time = now1.strftime("%d/%m/%Y %H:%M:%S")
        message="Jarvis(Bot)-> Hello Today's date and time: " + dt_time

    elif str_check:
        click=str_check
        #print(click)
        uname.append(str_check)
        socketio.emit('new address', {      #to get the clickable link
        'keylink': click
        })
    #print(data["address"])
    string=len(message)
    #print(string)
    if string == 0:
        db.session.add(models.Usps(data["address"] +" "+ dt_string))
        db.session.commit()
        emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
        return ": " + data["address"]
    else:
        db.session.add(models.Usps(data["address"] +" "+ dt_string))
        db.session.add(models.Usps(message))
        db.session.commit()
        return message
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)

@app.route('/')
def index():
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)

    return flask.render_template("index.html")
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
