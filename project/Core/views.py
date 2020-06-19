from flask import render_template, Blueprint, redirect, url_for, flash
from project.Core.forms import ContactUs
from project.modles import Contacts
from datetime import datetime
from project import db

core_blueprint = Blueprint('core', __name__)


@core_blueprint.route('/about')
def about():
    return render_template('about.html')


@core_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactUs()
    if form.validate_on_submit():

        user_feedback = Contacts(name=form.name.data, email=form.email.data,
                                 feedback=form.feedback.data, date=datetime.utcnow())
        db.session.add(user_feedback)
        db.session.commit()

        flash(f'form submitted by {form.name.data}', 'success')
        return redirect(url_for('core.contact'))

    return render_template('contact.html', form=form)
