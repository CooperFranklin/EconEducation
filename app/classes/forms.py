# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student"),("CEO","CEO"),("Gigachad","Gigacahd"),("Senior Manager","Senior Manager")])

class BlogForm(FlaskForm):
    content = TextAreaField('Response', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BlogForm2(FlaskForm):
    content = TextAreaField('Response', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class LessonForm(FlaskForm):
    lessonname = StringField("Lesson Name", validators=[DataRequired()])
    lessondescription = StringField("Lesson Description", validators=[DataRequired()])
    lessonurl = StringField('Lesson URL')
    lessonslide1 = URLField('Lesson Slide', validators=[DataRequired()])
    submit = SubmitField('Submit')

class QuizForm(FlaskForm):
    quiz1 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz2 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz3 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz4 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz5 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz6 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz7 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz8 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz9 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz10 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz11 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz12 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz13 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz14 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz15 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz16 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz17 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz18 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz19 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    quiz20 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    submit = SubmitField('Submit')

class QuizForm2(FlaskForm):
    quiz1 = StringField("Is this an Active or Passive investor?", validators=[DataRequired()])
    quiz2 = StringField("Is this an Active or Passive investor?", validators=[DataRequired()])
    quiz3 = StringField("Is this an Active or Passive investor?", validators=[DataRequired()])
    submit = SubmitField('Submit')

class QuizForm3(FlaskForm):
    quiz1 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz2 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz3 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz4 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz5 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz6 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz7 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz8 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz9 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz10 = StringField("What Industry is This?", validators=[DataRequired()])
    quiz11 = StringField("What Industry is This?", validators=[DataRequired()])
    submit = SubmitField('Submit')

class QuizForm4(FlaskForm):
    quiz1 = StringField("What is the Open price?", validators=[DataRequired()])
    quiz2 = StringField("What is the 52 week high?", validators=[DataRequired()])
    quiz3 = StringField("What is the P/E ratio?", validators=[DataRequired()])
    submit = SubmitField('Submit')