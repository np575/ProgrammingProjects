'''models.py'''
# pylint: disable=W0612
# pylint: disable=W0614
# pylint: disable=W0611
# pylint: disable=R0913
# pylint: disable=C0116
# pylint: disable=C0301
# pylint: disable=C0303
# pylint: disable=E1101
# pylint: disable=R0903
# pylint: disable=C0115
import flask_sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *

from app import db

class Users(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(30))
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(5))
    activityLevel = db.Column(db.Text)
    height = db.Column(db.Integer)
    date = db.Column(db.String(12))
    imgUrl = db.Column(db.Text)
    goal_weight = db.Column(db.Float)
    has_plan = db.Column(db.Boolean)
    weight = db.relationship('Weight', backref = 'users')
    messages = db.relationship('Chat', backref = 'users')
    workout = db.relationship('Workout', backref = 'users')
    
    
    # db.session.add(models.Users(email, name, birthday, gender, activityLevel))
    def __init__(self, email, name, height, birthday, gender, activityLevel, date, imgUrl, goal_weight):
        self.id = email
        self.name = name
        self.height = height
        self.birthday = birthday
        self.gender = gender
        self.activityLevel = activityLevel
        self.date = date
        self.imgUrl = imgUrl
        self.goal_weight= goal_weight
        self.has_plan = False
    def __repr__(self):
        return '<Email: %s\nName: %s\nHeight: %s\nBirthday: %s\nGender: %s\nActivity Level: %s \nGoal weight: %s>' % (self.id, self.name, self.height, self.birthday, self.gender, self.activityLevel,self.goal_weight)
        
class Weight(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.DateTime, primary_key=True)
    weight = db.Column(db.Float)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    # db.session.add(models.Weight(weight, email))
    def __init__(self, time, weight, email):
        self.id = time
        self.weight = weight
        self.email = email
        
    def __repr__(self):
        return '<Time: %s\nWeight: %s\nUser: %s>' % (self.time, self.weight, self.email)

class Macros(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    bmr = db.Column(db.Float)
    max_cal = db.Column(db.Float)
    min_cal = db.Column(db.Float)
    max_prot = db.Column(db.Float)
    min_prot = db.Column(db.Float)
    max_carb = db.Column(db.Float)
    min_carb = db.Column(db.Float)
    max_fat = db.Column(db.Float)
    min_fat = db.Column(db.Float)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    # db.session.add(models.Weight(weight, email))
    def __init__(self, bmr, max_cal, min_cal, max_prot, min_prot, max_carb, min_carb, max_fat, min_fat, email):
        self.bmr = bmr
        self.max_cal = max_cal
        self.min_cal = min_cal
        self.max_prot = max_prot
        self.min_prot = min_prot
        self.max_carb = max_carb
        self.min_carb = min_carb
        self.max_fat = max_fat
        self.min_fat = min_fat
        self.email = email
        
    def __repr__(self):
        return '<Bmr: %s\n Max Calories: %s\n Min Calories: %s\n Max Protein: %s\n Min Protein: %s\n Max Carbs: %s\n Min Carbs: %s\n Max Fat: %s\n Min Fat: %s\n User: %s>' % (self.bmr, 
        self.max_cal, self.min_cal, self.max_prot, self.min_prot, self.max_carb, self.min_carb, self.max_fat, self.min_fat, self.email)

class Meals(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    breakfast = db.Column(db.Text)
    lunch = db.Column(db.Text)
    dinner = db.Column(db.Text)
    meal_cal = db.Column(db.Float)
    meal_carb = db.Column(db.Float)
    meal_prot = db.Column(db.Float)
    meal_fat = db.Column(db.Float)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    # db.session.add(models.Weight(weight, email))
    def __init__(self, breakfast, lunch, dinner, meal_cal, meal_carb, meal_prot, meal_fat, email):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        self.meal_cal = meal_cal
        self.meal_carb = meal_carb
        self.meal_prot = meal_prot
        self.meal_fat = meal_fat
        self.email = email
        
    def __repr__(self):
        return '<Breakfast: %s\n Lunch: %s\n Dinner: %s\n Meal Calories: %s\n Meal Carbs: %s\n Meal Protein: %s\n Meal Fat: %s\n User: %s>' % (self.breakfast,
        self.lunch, self.dinner, self.meal_cal, self.meal_carb, self.meal_prot, self.meal_fat, self.email)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    time = db.Column(db.Text)
    user_id=db.Column(db.String(75),db.ForeignKey("users.id"))

    def __init__(self, text,time,user_id):
        self.text = text
        self.time = time
        self.user_id = user_id
        
    def __repr__(self):
        return '<Chat messages: %s>' % self.text
        
class Workout(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    split = db.Column(db.Text)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    def __init__(self, level,split, email):
        self.level = level
        self.split = split
        self.email = email
    
    def __repr__(self):
        return '<level: %s \n split: %s>' % (self.level, self.split)

    
db.create_all()
db.session.commit()