from flask import g, session
from app import db

g = g
session = session
def add_user_to_g(user):
    if user:
        g.user = user
    else:
        g.user = None
   

def create_session():
    if g.user:
        session["current_user"] = g.user.userID
   

def user_logout():
   if session["current_user"]:
        del session["current_user"]
        g.user =None
