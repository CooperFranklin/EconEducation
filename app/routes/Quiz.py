from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Quiz1
from app.classes.forms import QuizForm
from flask_login import login_required
import datetime as dt

@app.route('/quiz/quiz1', methods=['GET','POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def quiz1():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = QuizForm()
    print("YOOOOOO WHATS GOOOD")

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new blog form. 
        # Blog() is a mongoengine method for creating a new blog. 'newBlog' is the variable 
        # that stores the object that is the result of the Blog() method.  
        Answers = Quiz1(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            Quiz1 = form.Quiz1.data,
            Quiz2 = form.Quiz2.data,
            Quiz3 = form.Quiz3.data,
            Quiz4 = form.Quiz4.data,
            Quiz5 = form.Quiz5.data,
            Quiz6 = form.Quiz6.data,
            Quiz7 = form.Quiz7.data,
            Quiz8 = form.Quiz8.data,
            Quiz9 = form.Quiz9.data,
            Quiz10 = form.Quiz10.data,
            Quiz11 = form.Quiz11.data,
            Quiz12 = form.Quiz12.data,
            Quiz13 = form.Quiz13.data,
            Quiz14 = form.Quiz14.data,
            Quiz15 = form.Quiz15.data,
            Quiz16 = form.Quiz16.data,
            Quiz17 = form.Quiz17.data,
            Quiz18 = form.Quiz18.data,
            Quiz19 = form.Quiz19.data,
            Quiz20 = form.Quiz20.data,
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        Answers.save()

        # Once the new blog is saved, this sends the user to that blog using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a blog so we want 
        # to send them to that blog. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return redirect(url_for('quiz1',QuizID=Answers.id))

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at blogform.html to 
    # see how that works.
    print("YOOOOOO WHATS GOOOD")
    return render_template('Quiz1_form.html',form=form)

