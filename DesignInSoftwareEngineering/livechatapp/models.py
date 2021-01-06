# models.py
# pylint: disable=E1101
# pylint: disable=C0303
# pylint: disable=C0115
import flask_sqlalchemy
from app import db


class Usps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    
    def __init__(self, a):
        self.address = a
        
    def __repr__(self):
        return '<Usps address: %s>' % self.address 
        

class AuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    auth_type = db.Column(db.String(120)) 
    name = db.Column(db.String(120)) 
    image = db.Column(db.String(650)) 
    email = db.Column(db.String(500)) 



