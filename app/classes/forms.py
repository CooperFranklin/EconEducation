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
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class LessonForm(FlaskForm):
    lessonname = StringField("Lesson Name", validators=[DataRequired()])
    lessondescription = StringField("Lesson Description", validators=[DataRequired()])
    lessonurl = StringField('Lesson URL', validators=[DataRequired()])
    lessonslide1 = URLField('Lesson Slide', validators=[DataRequired()])
    submit = SubmitField('Submit')

class QuizForm(FlaskForm):
    Quiz1 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz2 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz3 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz4 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz5 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz6 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz7 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz8 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz9 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz10 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz11 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz12 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz13 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz14 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz15 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz16 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz17 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz18 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz19 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz20 = StringField("What Does This Picture Represent?", validators=[DataRequired()])
    Quiz21= StringField("What Does This Picture Represent?", validators=[DataRequired()])
    
