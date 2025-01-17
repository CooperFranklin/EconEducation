# This is where all the database collections are defined. A collection is a place to hold a defined 
# set of data like Users, Blogs, Comments. Collections are defined below as classes. Each class name is 
# the name of the data collection and each item is a data 'field' that stores a piece of data.  Data 
# fields have types like IntField, StringField etc.  This uses the Mongoengine Python Library. When 
# you interact with the data you are creating an onject that is an instance of the class.

from sys import getprofile
from tokenize import String
from typing import KeysView
from xmlrpc.client import Boolean

from setuptools import SetuptoolsDeprecationWarning
from app import app
from flask import flash
from flask_login import UserMixin
from mongoengine import FileField, EmailField, StringField, IntField, ReferenceField, DateTimeField, BooleanField, CASCADE
from flask_mongoengine import Document
import datetime as dt
import jwt
from time import time
from bson.objectid import ObjectId

class User(UserMixin, Document):
    createdate = DateTimeField(defaultdefault=dt.datetime.utcnow)
    gid = StringField(sparse=True, unique=True)
    gname = StringField()
    gprofile_pic = StringField()
    username = StringField()
    fname = StringField()
    lname = StringField()
    email = EmailField()
    image = FileField()
    prononuns = StringField()
    role = StringField()

    meta = {
        'ordering': ['lname','fname']
    }
    
class Blog(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()


    meta = {
        'ordering': ['-createdate']
    }

class Blog2(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()


    meta = {
        'ordering': ['-createdate']
    }


class Comment(Document):
    # Line 63 is a way to access all the information in Course and Teacher w/o storing it in this class
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    blog = ReferenceField('Blog',reverse_delete_rule=CASCADE)
    # This could be used to allow comments on comments
    comment = ReferenceField('Comment',reverse_delete_rule=CASCADE)
    # Line 68 is where you store all the info you need but won't find in the Course and Teacher Object
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Lesson(Document):
    author = ReferenceField('User', reverse_delete_rule=CASCADE)
    lessonname = StringField()
    lessondescription = StringField()
    lessonurl = StringField()
    lessonslide1=StringField()
    lessonquestion=StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Quiz1(Document):
    quiz1=BooleanField()
    quiz2=BooleanField()
    quiz3=BooleanField()
    quiz4=BooleanField()
    quiz5=BooleanField()
    quiz6=BooleanField()
    quiz7=BooleanField()
    quiz8=BooleanField()
    quiz9=BooleanField()
    quiz10=BooleanField()
    quiz11=BooleanField()
    quiz12=BooleanField()
    quiz13=BooleanField()
    quiz14=BooleanField()
    quiz15=BooleanField()
    quiz16=BooleanField()
    quiz17=BooleanField()
    quiz18=BooleanField()
    quiz19=BooleanField()
    quiz20=BooleanField()
    
    

    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Quiz2(Document):
    quiz1=BooleanField()
    quiz2=BooleanField()
    quiz3=BooleanField()
    
    

    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Quiz3(Document):
    quiz1=BooleanField()
    quiz2=BooleanField()
    quiz3=BooleanField()
    quiz4=BooleanField()
    quiz5=BooleanField()
    quiz6=BooleanField()
    quiz7=BooleanField()
    quiz8=BooleanField()
    quiz9=BooleanField()
    quiz10=BooleanField()
    quiz11=BooleanField()
    
    

    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Quiz4(Document):
    quiz1=BooleanField()
    quiz2=BooleanField()
    quiz3=BooleanField()
    
    

    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }