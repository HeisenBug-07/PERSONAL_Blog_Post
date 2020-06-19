from project import app
from flask import render_template, request
from project.modles import Posts
from sqlalchemy import desc


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    page = request.args.get('page', 1, type=int)
    post = Posts.query.order_by(desc(Posts.s_no)).paginate(page=page, per_page=3)
    return render_template('home.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)

