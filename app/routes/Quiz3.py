from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Quiz3
from app.classes.forms import QuizForm3
from flask_login import login_required
import datetime as dt

rightAnswers = {
    "quiz1":"Materials", "quiz2":"Industrials", "quiz3":"Communication Services","quiz4":"Healthcare","quiz5":"Consumer Staples","quiz6":"Utilities","quiz7":"Information Technology","quiz8":"Energy","quiz9":"Consumer Discretionary","quiz10":"Real Estate","quiz11":"Financials"
}

@app.route('/quiz3/quiz3', methods=['GET','POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def quiz3():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = QuizForm3()
    Quest1 = "False"
    Quest2 = "False"
    Quest3 = "False"
    Quest4 = "False"
    Quest5 = "False"
    Quest6 = "False"
    Quest7 = "False"
    Quest8 = "False"
    Quest9 = "False"
    Quest10 = "False"
    Quest11 = "False"
    QuestionsList = [Quest1,Quest2,Quest3,Quest4,Quest5,Quest6,Quest7,Quest8,Quest9,Quest10,Quest11]
    


    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new blog form. 
        # Blog() is a mongoengine method for creating a new blog. 'newBlog' is the variable 
        # that stores the object that is the result of the Blog() method.  
        Answers = Quiz3(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            quiz1 = (rightAnswers['quiz1'] == form.quiz1.data),
            quiz2 = (rightAnswers['quiz2'] == form.quiz2.data),
            quiz3 = (rightAnswers['quiz3'] == form.quiz3.data),
            quiz4 = (rightAnswers['quiz4'] == form.quiz4.data),
            quiz5 = (rightAnswers['quiz5'] == form.quiz5.data),
            quiz6 = (rightAnswers['quiz6'] == form.quiz6.data),
            quiz7 = (rightAnswers['quiz7'] == form.quiz7.data),
            quiz8 = (rightAnswers['quiz8'] == form.quiz8.data),
            quiz9 = (rightAnswers['quiz9'] == form.quiz9.data),
            quiz10 = (rightAnswers['quiz10'] == form.quiz10.data),
            quiz11 = (rightAnswers['quiz11'] == form.quiz11.data),
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        Answers.save()
        

        for i,answer in enumerate(Answers):
            if Answers[answer] == True:
                print(i)
                QuestionsList[i-1] = "True"
        # Once the new blog is saved, this sends the user to that blog using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a blog so we want 
        # to send them to that blog. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return render_template('results.html',Answers=Answers, QuestionsList=QuestionsList)

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at blogform.html to 
    # see how that works.
    
    return render_template('Quiz_form3.html',form=form)

