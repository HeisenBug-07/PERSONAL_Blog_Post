from flask import redirect, render_template,flash, url_for, Blueprint, session, request
from project.Admin.forms import LoginForm
from project.modles import Posts, Contacts
from sqlalchemy import desc
from project import db

admin_blueprint = Blueprint('admin', __name__, template_folder='templates/Admin')


@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if 'admin' in session and session['admin'] == 'King':
        return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == 'shubham' and form.email.data == 'shubhamroyal17@gmail.com':
            session['admin'] = 'King'
            flash('You are logged in !', 'success')
            return redirect(url_for('admin.dashboard'))

    return render_template('login.html', form=form)


@admin_blueprint.route('/dashboard')
def dashboard():
    if 'admin' in session and session['admin'] == 'King':
        post = Posts.query.order_by(desc(Posts.s_no)).all()
        return render_template('dashboard.html', post=post)
    return redirect(url_for('admin.login'))


@admin_blueprint.route('/read_feedback')
def read_feedback():
    if 'admin' in session and session['admin'] == 'King':
        page = request.args.get('page', 1, type=int)
        feedback = Contacts.query.order_by(desc(Contacts.s_no)).paginate(page=page, per_page=3)
        return render_template('read_feedback.html', feedback=feedback)
    return redirect(url_for('admin.login'))


@admin_blueprint.route('/delete_feedback/<string:sno>', methods=['GET', 'POST'])
def delete_feedback(sno):
    if 'admin' in session and session['admin'] == 'King':
        feedback = Contacts.query.filter_by(s_no=sno).first()
        db.session.delete(feedback)
        db.session.commit()
        flash(f'feedback deleted : {feedback.name}', 'danger')
        return redirect(url_for('admin.read_feedback'))
    return redirect(url_for('admin.login'))


@admin_blueprint.route('/logout')
def logout():
    if 'admin' in session and session['admin'] == 'King':
        session.pop('admin')
        flash('you are logged out !!', 'danger')
        return redirect(url_for('home'))
    return redirect('admin.login')
