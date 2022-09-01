from flask import Flask, jsonify, abort
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


@app.route('/posts/<int:post_id>')
def get_specific_post(post_id):
    post = Post.query.filter(Post.post_id==post_id).one_or_none()

    try:
        if post is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'post': post.format()
            })
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.debug = True
    app.run()