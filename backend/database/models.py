import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from flask_cors import CORS
from flask_migrate import Migrate

DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_USER = os.getenv('DB_USER', 'student')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'student')
DB_NAME = os.getenv('DB_NAME', 'stdb')
DB_PATH = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

db = SQLAlchemy()
migrate = Migrate()

"""
setup_db(app)
    binds a flask application and a SQALchemy service
"""
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    
    #db.create_all() """I will use migrations instead"""

"""
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
"""
# def db_drop_and_create_all():
#     db.drop_all()
#     db.create_all()

