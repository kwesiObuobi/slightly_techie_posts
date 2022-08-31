from flask import Flask
from flask_cors import CORS
from database.models import setup_db, Post

app = Flask(__name__)
CORS(app)
setup_db(app)

@app.route('/')
def index():
    return "Smiley me => :)"


if __name__ == '__main__':
    app.debug = True
    app.run()