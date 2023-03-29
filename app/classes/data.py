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
    subject = StringField()
    content = StringField()
    tag = StringField()
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
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Quiz1(Document):
    Question1=StringField()
    Question2=StringField()
    Question3=StringField()
    Question4=StringField()
    Question5=StringField()
    Question6=StringField()
    Question7=StringField()
    Question1=StringField()
    Question2=StringField()
    Question3=StringField()
    Question4=StringField()
    Question5=StringField()
    Question6=StringField()
    Question7=StringField()
    Question8=StringField()
    Question9=StringField()
    Question10=StringField()
    Question11=StringField()
    Question12=StringField()
    Question13=StringField()
    Question14=StringField()
    Question15=StringField()
    Question16=StringField()
    Question17=StringField()
    Question18=StringField()
    Question19=StringField()
    Question20=StringField()
    Question21=StringField()

    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }