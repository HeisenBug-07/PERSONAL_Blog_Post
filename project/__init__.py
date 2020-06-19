import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'killer_B_123321!@#)(*'

dir_name = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir_name, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

from project.Core.views import core_blueprint
from project.Post.views import post_blueprint
from project.Admin.views import admin_blueprint
from project.error.handler import error_blueprint

app.register_blueprint(core_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(error_blueprint)