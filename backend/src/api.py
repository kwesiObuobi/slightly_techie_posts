from flask import Flask, jsonify
from flask_cors import CORS
from database.models import setup_db, Post

app = Flask(__name__)
CORS(app)
setup_db(app)

@app.route('/')
def index():
    return "Smiley me => :)"

@app.route('/posts')
def get_posts():
    posts = Post.query.all()
    formatted_posts = [post.format() for post in posts]

    return jsonify({
        'success': True,
        'posts': formatted_posts,
        'total_posts': len(formatted_posts)
    })


if __name__ == '__main__':
    app.debug = True
    app.run()