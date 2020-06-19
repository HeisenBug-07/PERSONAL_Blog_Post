from project import db
from datetime import datetime


class Posts(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.String, default='default_image.jpg')
    content = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.date)

    def __init__(self, title, image, content, date, slug):
        self.title = title
        self.image = image
        self.content = content
        self.date = date
        self.slug = slug


class Contacts(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    feedback = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.date)

    def __init__(self, name, email, feedback, date):
        self.name = name
        self.email = email
        self.feedback = feedback
        self.date = date
