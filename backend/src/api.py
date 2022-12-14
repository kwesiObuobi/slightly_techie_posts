from flask import Flask, request, redirect, url_for, jsonify, abort
from flask_cors import CORS
from database.models import setup_db, Post

app = Flask(__name__)
setup_db(app)
# CORS(app, resources={r'*': {'origins': '*'}})
CORS(app)


"""
Use the after_request decorator to set Access-Control-Allow.
List of all HTTP request header values the server will allow
List of all HTTP request types allowed on these backend resources
"""
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, GET, PATCH, DELETE')
    return response


"""
Home route. Redirected to the endpoint which retrieves all posts
"""
@app.route('/')
def index():
    return redirect(url_for('create_post'))


"""
Endpoint for creating posts
"""
@app.route('/posts', methods=['POST'])
def create_post():
    body = request.get_json()

    new_title = body.get('title', None)
    new_text = body.get('text', None)

    try:
        post = Post(title = new_title, text = new_text)
        post.insert()

        posts  = [post.format() for post in Post.query.order_by(Post.post_id).all()]

        return jsonify({
            'success': True,
            'created_post_id': post.post_id,
            'posts': posts,
            'total_posts': len(posts)
        })
    except:
        abort(422)


"""
Endpoint for updating a post
"""
@app.route('/posts/<int:post_id>', methods=['PATCH'])
def update_post(post_id):
    body = request.get_json()

    try:
        post = Post.query.filter(Post.post_id == post_id).one_or_none()
        
        if post is None:
            abort(404)

        if 'title' in body:
            post.title = body.get('title')
        
        if 'text' in body:
            post.text = body.get('text')

        post.update()

        return jsonify({
            'success': True,
            'updated_id': post.post_id
        })
    
    except:
        abort(400)


"""
Endpoint for deleting a post
"""
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        post = Post.query.filter(Post.post_id == post_id).one_or_none()

        if post is None:
            abort(404)
        
        post.delete()
        return jsonify({
            'success': True,
            'deleted_id': post_id
        })

    except:
        abort(422)


"""
Endpoint for viewing all posts
"""
@app.route('/posts')
def get_posts():
    posts = Post.query.all()
    formatted_posts = [post.format() for post in posts]

    return jsonify({
        'success': True,
        'posts': formatted_posts,
        'total_posts': len(formatted_posts)
    })


"""
Endpoint for viewing a single post
"""
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

    except:
        abort(404)


"""
Error handlers for all expected errors
"""
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'bad request'
    }), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404

@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }), 405

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'unprocessable'
    }), 422

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'internal server error'
    }), 500
    

if __name__ == '__main__':
    app.debug = True
    app.run()