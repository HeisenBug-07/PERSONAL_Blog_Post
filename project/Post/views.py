from flask import render_template, flash, redirect, url_for, Blueprint, current_app, session, request
from project.Post.forms import AddPosts, UpdatePosts
from project.modles import Posts
from datetime import datetime
from project import db
import os

post_blueprint = Blueprint('post', __name__, template_folder='templates/Post')


def pic_uploader(pic_upload):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    store_filename = str(filename) + '.' + ext_type
    file_path = os.path.join(current_app.root_path, 'static\images', store_filename)
    pic_upload.save(file_path)
    return store_filename


@post_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    if 'admin' in session and session['admin'] == 'King':
        form = AddPosts()
        if form.validate_on_submit():
            if form.image.data:
                pic = pic_uploader(form.image.data)
                post = Posts(title=form.title.data, image=pic, content=form.content.data,
                             date=datetime.utcnow(), slug=form.title.data)
                db.session.add(post)
                db.session.commit()
                flash(f'{form.title.data} created', 'success')
                return redirect(url_for('admin.dashboard'))

        return render_template('add.html', form=form)
    return redirect(url_for('admin.login'))


@post_blueprint.route('/update/<string:sno>', methods=['GET', 'POST'])
def update(sno):
    if 'admin' in session and session['admin'] == 'King':
        form = UpdatePosts()
        post = Posts.query.filter_by(s_no=sno).first()
        if form.validate_on_submit():
            if form.image.data:
                pic = pic_uploader(form.image.data)
                post.title = form.title.data
                post.image = pic
                post.content = form.content.data
                post.slug = form.title.data
                db.session.commit()
                flash(f'{form.title.data} updated', 'success')
                return redirect(url_for('admin.dashboard'))

        elif request.method == 'GET':
            form.title.data = post.title
            form.image.data = post.image
            form.content.data = post.content

        return render_template('update.html', form=form, post=post)
    return redirect(url_for('admin.login'))


@post_blueprint.route('/read/<string:slug>', methods=['GET', 'POST'])
def read(slug):
    post = Posts.query.filter_by(slug=slug).first()
    return render_template('read.html', post=post)


@post_blueprint.route('/delete/<string:sno>')
def delete(sno):
    if 'admin' in session and session['admin'] == 'King':
        post = Posts.query.filter_by(s_no=sno).first()
        db.session.delete(post)
        db.session.commit()
        flash(f'{post.title} deleted', 'danger')
        return redirect(url_for('admin.dashboard'))
    return redirect(url_for('admin.login'))
