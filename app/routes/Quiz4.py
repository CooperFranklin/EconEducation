from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Quiz4
from app.classes.forms import QuizForm4
from flask_login import login_required
import datetime as dt

rightAnswers = {
    "quiz1":"252.19", "quiz2":"315.95", "quiz3":"27.85"
}

@app.route('/quiz4/quiz4', methods=['GET','POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def quiz4():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = QuizForm4()
    Quest1 = "False"
    Quest2 = "False"
    Quest3 = "False"
    QuestionsList = [Quest1,Quest2,Quest3]
    


    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new blog form. 
        # Blog() is a mongoengine method for creating a new blog. 'newBlog' is the variable 
        # that stores the object that is the result of the Blog() method.  
        Answers = Quiz4(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            quiz1 = (rightAnswers['quiz1'] == form.quiz1.data),
            quiz2 = (rightAnswers['quiz2'] == form.quiz2.data),
            quiz3 = (rightAnswers['quiz3'] == form.quiz3.data),
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        Answers.save()
        print(Answers.quiz1)

        for i,answer in enumerate(Answers):
            if Answers[answer] == True:
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
    
    return render_template('Quiz_form4.html',form=form)

