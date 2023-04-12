from flask import render_template, redirect, url_for, flash
from app import application  # Importing the application module.
from app.forms import SignUpForm  # Importing the SignUpForm class function from the forms.py file
from google.cloud import datastore, pubsub_v1

# Firestore
db = datastore.Client()
kind = 'signuptable'


@application.route('/')
@application.route('/home')  # Routing the default page and home page to the home.html file.
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        key = db.key(kind)
        entity = datastore.Entity(key=key)
        entity.update({
            'name': form.name.data, 'email': form.email.data,
            'mobile': form.mobile.data, 'country': form.country.data,
            'newsletter': form.newsletter.data
        })  
        db.put(entity) # Putting the users information into the Datastore entity

        msg = 'Congratulations !!! {} is now a Premium Member !'.format(form.name.data)
        flash(msg)  # Creates a pop-up message when the form is successfully saved

        return redirect(url_for('home_page'))  # Redirect user to the home page

    return render_template('signup.html', form=form)  # Return the signup.html page

