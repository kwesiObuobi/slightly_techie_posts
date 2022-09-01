import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
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

    """
    You should uncomment the below code once - on first server run;
    to get the database freshly setup, and with an initial database record.
    """
    #db_drop_and_create_all()
    

"""
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
"""
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

    # create a demo post for testing purposes
    demo_post = Post(title="Slightly Techie", text="This is just a team of devs trying to be better")
    demo_post.insert()


######################################
# MODELS
######################################

"""Post class"""
class Post(db.Model):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "post_id": self.post_id,
            "title": self.title,
            "text": self.text
        }

