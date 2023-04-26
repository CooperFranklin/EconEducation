from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Quiz1
from app.classes.forms import QuizForm
from flask_login import login_required
import datetime as dt

rightAnswers = {
    "quiz1":"Market Open", "quiz2":"Market Close", "quiz3":"Market High","quiz4":"Market Low","quiz5":"Bullish","quiz6":"Bearish","quiz7":"Share","quiz8":"Trade","quiz9":"Ticker","quiz10":"Quantity","quiz11":"ETF","quiz12":"Index Fund","quiz13":"Volume","quiz14":"PE Ratio","quiz15":"IPO","quiz16":"Ask","quiz17":"Bid","quiz18":"Market Cap","quiz19":"Market Price","quiz20":"Limit Order"
}

@app.route('/quiz/quiz1', methods=['GET','POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def quiz1():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = QuizForm()
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
    Quest12 = "False"
    Quest13 = "False"
    Quest14 = "False"
    Quest15 = "False"
    Quest16 = "False"
    Quest17 = "False"
    Quest18 = "False"
    Quest19 = "False"
    Quest20 = "False"
    QuestionsList = [Quest1,Quest2,Quest3,Quest4,Quest5,Quest6,Quest7,Quest8,Quest9,Quest10,Quest11,Quest12,Quest13,Quest14,Quest15,Quest16,Quest17,Quest18,Quest19,Quest20]
    


    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new blog form. 
        # Blog() is a mongoengine method for creating a new blog. 'newBlog' is the variable 
        # that stores the object that is the result of the Blog() method.  
        Answers = Quiz1(
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
            quiz12 = (rightAnswers['quiz12'] == form.quiz12.data),
            quiz13 = (rightAnswers['quiz13'] == form.quiz13.data),
            quiz14 = (rightAnswers['quiz14'] == form.quiz14.data),
            quiz15 = (rightAnswers['quiz15'] == form.quiz15.data),
            quiz16 = (rightAnswers['quiz16'] == form.quiz16.data),
            quiz17 = (rightAnswers['quiz17'] == form.quiz17.data),
            quiz18 = (rightAnswers['quiz18'] == form.quiz18.data),
            quiz19 = (rightAnswers['quiz19'] == form.quiz19.data),
            quiz20 = (rightAnswers['quiz20'] == form.quiz20.data),
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        Answers.save()
        print(Answers.quiz1)

        for i,answer in enumerate(Answers):
            if answer == True:
                QuestionsList[i] = "True"
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
    
    return render_template('Quiz1_form.html',form=form)

