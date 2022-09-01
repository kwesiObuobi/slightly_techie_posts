# Getting Started

## Pre-requisites and Local Development

### Setting up the backend

1. Install Dependencies

* **Python 3.10** - Follow instructions to install the latest version of python 3 for your platform. Visit the [python docs](https://www.python.org/).

* **Virtual Environment and PIP dependencies** - Virtual envrionements are recommended whenever python is being used for projects. This keeps your dependecies separate and organized for each project. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

* **PIP Dependencies** - Once your virtual environment is set up and running, install the required dependencies by navigating to the `/backend` directory and running:

> **Note** - Ensure you are in your virtual environment.

```bash
pip install -r requirements.txt
```
<br/>
2. Set up the Database

* With postgres running, create a database called `stdb`

```bash
createbd stdb
```

* In `/backend/database/models.py`, uncomment the `db_drop_and_create_all()` method which creates `posts` table in the database, and inserts a single record for demo/testing purposes. After a first successful run of the project, you should go back and comment out the `db_drop_and_create_all()` method in order to save your new record inserts.

<br/>
3. Run the server

Ensure you are within the `/backend` directory and you're working using your created virtual environment

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_DEBUG=True
export FLASK_ENV=development
flask run --reload
```


<br/> <br/> <br/> 

# API Reference

## Getting Started

* Base URL: At present this application can only be run locally. The backend app is hosted at the default, `http://127.0.0.1:5000/`.

## Error Handling

Errors are returned as JSON objects in the following format:
```
{
    'success': False,
    'error': 405,
    'message': 'method not allowed'
}
```

The API returns five error types when requests fail. They are:
* 400: Bad Request
* 404: Resource Not Found
* 405: Method Not Allowed
* 422: Not Processable
* 500: Internal Server Error

## Endpoints

### POST /posts

* This endpoint creates a new post and adds it to the database. The new post must have a title and a text. The endpoint returns the id of the new post, the posts available in the database, the total number of posts in the database, and a success value.
* Sample: `curl -X POST -H "Content-Type: application/json" -d '{"title": "Slightly Techie", "text": "Just a group of devs trying to be better"}' http://127.0.0.1:5000/posts`

```
{
    "created_post_id": 3,
    "posts": [
        {
            "post_id": 1,
            "text": "This is just a team of devs trying to be better",
            "title": "Slightly techie1"
        },
        {
            "post_id": 2,
            "text": "My next destination",
            "title": "Microsoft"
        },
        {
            "post_id": 3,
            "text": "Right after Microsoft",
            "title": "Google"
        }
    ],
    "success": true,
    "total_posts": 3
}
```

### PATCH /posts/{post_id}

* This endpoint updates a post given by the ID. It returns a success value and the ID of the post that has been updated.
* Sample: `curl http://127.0.0.1:5000/posts/2 -X PATCH -H "Content-Type: application/json" -d '{"title": "Amazon", "text": "Our new next destination"}'`

```
{
    "success": true,
    "updated_id": 2
}
```

### DELETE /posts/{post_id}

* Deletes a post given by the ID. It returns a success value and the ID of the post that has been deleted.
* sample: `curl -X DELETE http://127.0.0.1:5000/posts/3`

```
{
    "deleted_id": 3,
    "success": true
}
```

### GET /posts

* This endpoint returns all posts available in the database, a success value, and the total number of posts in the database
* Sample: `curl http://127.0.0.1:5000/posts`

```
{
    "posts": [
        {
            "post_id": 1,
            "text": "This is just a team of devs trying to be better",
            "title": "Slightly Techie"
        },
        {
            "post_id": 2,
            "text": "My next destination",
            "title": "Microsoft"
        },
        {
            "post_id": 3,
            "text": "Right after Microsoft",
            "title": "Google"
        }
    ],
    "success": true,
    "total_posts": 3
}
```

### GET /posts/{post_id}

* This endpoint returns a specific post given by the ID. It also returns a success value.
* Sample: `curl http://127.0.0.1:5000/posts/2`

```
{
    "post": {
        "post_id": 2,
        "text": "My next destination",
        "title": "Microsoft"
    },
    "success": true
}
```

