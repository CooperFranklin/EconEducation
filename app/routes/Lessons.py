from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Lesson
from app.classes.forms import LessonForm
from flask_login import login_required
import datetime as dt

@app.route('/lesson/new', methods=['GET', 'POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def lessonNew():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = LessonForm()
    print(form)

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new blog form. 
        # Blog() is a mongoengine method for creating a new blog. 'newBlog' is the variable 
        # that stores the object that is the result of the Blog() method.  
        newLesson = Lesson(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            lessonname = form.lessonname.data,
            lessondescription = form.lessondescription.data,
            lessonurl =form.lessonurl.data,
            author = current_user.id,
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        newLesson.save()

        # Once the new blog is saved, this sends the user to that blog using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a blog so we want 
        # to send them to that blog. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return redirect(url_for('lesson',lessonID=newLesson.id))

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at blogform.html to 
    # see how that works.
    return render_template('lesson_form.html',form=form)

@app.route('/lesson/<lessonID>')
# This route will only run if the user is logged in.
@login_required
def lesson(lessonID):
    # retrieve the blog using the blogID
    thisLesson = Lesson.objects.get(id=lessonID)
    # If there are no comments the 'comments' object will have the value 'None'. Comments are 
    # related to blogs meaning that every comment contains a reference to a blog. In this case
    # there is a field on the comment collection called 'blog' that is a reference the Blog
    # document it is related to.  You can use the blogID to get the blog and then you can use
    # the blog object (thisBlog in this case) to get all the comments.
    # Send the blog object and the comments object to the 'blog.html' template.
    return render_template('Lesson.html',lesson=thisLesson)

@app.route('/lesson/list')
@app.route('/lesson')
# This means the user must be logged in to see this page
@login_required
def lessonList():
    # This retrieves all of the 'blogs' that are stored in MongoDB and places them in a
    # mongoengine object as a list of dictionaries name 'blogs'.
    lessons = Lesson.objects()
    # This renders (shows to the user) the blogs.html template. it also sends the blogs object 
    # to the template as a variable named blogs.  The template uses a for loop to display
    # each blog.
    return render_template('lessons.html',lessons=lessons)

@app.route('/lesson/edit/<lessonID>', methods=['GET', 'POST'])
@login_required
def lessonEdit(lessonID):
    editLesson = Lesson.objects.get(id=lessonID)
    # if the user that requested to edit this blog is not the author then deny them and
    # send them back to the blog. If True, this will exit the route completely and none
    # of the rest of the route will be run.
    if current_user != editLesson.author:
        flash("You can't edit a lesson you don't own.")
        return redirect(url_for('lesson',lessonID=lessonID))
    # get the form object
    form = LessonForm()
    # If the user has submitted the form then update the blog.
    if form.validate_on_submit():
        # update() is mongoengine method for updating an existing document with new data.
        editLesson.update(
            lessonname = form.lessonname.data,
            lessondescription = form.lessondescription.data,
            lessonurl =form.lessonurl.data,
            modify_date = dt.datetime.utcnow
        )
        # After updating the document, send the user to the updated blog using a redirect.
        return redirect(url_for('lesson',lessonID=lessonID))

    # if the form has NOT been submitted then take the data from the editBlog object
    # and place it in the form object so it will be displayed to the user on the template.
    form.lessonname.data = editLesson.lessonname
    form.lessondescription.data = editLesson.lessondescription
    form.lessonurl.data = editLesson.lessonurl


    # Send the user to the blog form that is now filled out with the current information
    # from the form.
    return render_template('lesson_form.html',form=form)

@app.route('/lesson/delete/<lessonID>')
# Only run this route if the user is logged in.
@login_required
def lessonDelete(lessonID):
    # retrieve the blog to be deleted using the blogID
    deleteLesson = Lesson.objects.get(id=lessonID)
    # check to see if the user that is making this request is the author of the blog.
    # current_user is a variable provided by the 'flask_login' library.
    if current_user == deleteLesson.author:
        # delete the blog using the delete() method from Mongoengine
        deleteLesson.delete()
        # send a message to the user that the blog was deleted.
        flash('The Lesson was deleted.')
    else:
        # if the user is not the author tell them they were denied.
        flash("You can't delete a lesson you don't own.")
    # Retrieve all of the remaining blogs so that they can be listed.
    lessons = Lesson.objects()  
    # Send the user to the list of remaining blogs.
    return render_template('lessons.html',lessons=lessons)