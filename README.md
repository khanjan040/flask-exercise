# Flask Exercise

This exercise is intended for you to get familiar with fundamental backend/server side programming in an interactive way, as well as for you to get comfortable developing in a modern Python/Flask environment.

Reading the following will help you get a sense of the big picture when it comes to developing APIs/writing server side code, and how it fits in the context of a larger web application:

- [How the Web Works](https://medium.freecodecamp.org/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c) - Read all 3 parts, especially part 3!
- [Basics of HTTP](https://egghead.io/courses/understand-the-basics-of-http)

This project will be broken down into multiple parts. After you finish this project, you must submit your repository link to me.

This exercise's first part is due by today EOD, February 21st.

### Requirements

- python version 3.x
- pip
- conda
- [Postman](https://www.getpostman.com/)

### Setup

First, fork this repository. The fork button on your top right. What this does is copies this repository over to your account. Now you should have a repository with the name `<yourusername>/flask-exercise`.

Then, clone this repository (click the green button saying "Clone or Download", choose http, and copy and paste it the location `<url>` ) and go into it:

```
$ git clone <url>
$ cd flask-exercise
```

Then, setup your virtual environment and install the python dependencies required to run this app. We use conda, which automatically sets everything up for the environment according to specific python version.

Follow these following steps in `Anaconda Shell`:

1. Creating environment with name: `flask-task`

   ```
   conda create -n flask-task python=3.8
   ```

2. Activate the environment

   ```
   conda activate flask-task
   ```

3. Install dependencies (you should be in the same directory as the `requirements.txt` file)

   ```
   pip install -r requirements.txt
   ```

4. Start flask server (you should be in the same directory as the `app.py` file)
   ```
   python app.py
   ```

- Note: This will remain a running process in your terminal, so you will need to open a new tab or window to execute other commands.

- To stop the server, press `Control-C`.

- To exit your virtual environment, run:

  ```
  conda deactivate
  ```

Before you make any changes to the code, make sure to create a new branch. Typically branches are named based on the feature or bugfix being addressed, but for this project, create a new branch: `dev`:

```
git checkout -b dev
```

- Branch names should be all lowercase and can't contain spaces. Instead of spaces, use hyphens. For example:

  ```
  git checkout -b dev-2
  ```

### Running The Server And Calling Endpoints

Starting the server will make it a continuously running process on `127.0.0.1:5000`. In order to make requests to your server, use [Postman](https://www.getpostman.com/).

First, make a `GET` request to the `/` endpoint. Since the server is running on `127.0.0.1:5000`, the full endpoint url is `127.0.0.1:5000/`.

Try calling the `/mirror` endpoint. First, look at the code for the endpoint to see how you can specify url parameters. Then make a request on Postman to `127.0.0.1:5000/mirror/<name>`:

# Exercises

These exercises will walk you through creating a RESTful API using Flask! We don't want you to go through all the hassle of setting up a database instance, so we have created dummy data and a mock database interface to interact with it. For the sake of ease, the entire app logic minus the mockdb logic will by implemented in `app.py`. For larger projects, the API endpoints will usually be separated out into different files called `views`.

Before you start, take a good look at the `create_response` function and how it works. Make sure you follow the guidelines for how to use this function, otherwise your API will not follow the proper conventions!

Also take a look into the mock database. The initial dummy data is defined in `mockdb/dummy_data.py`. This is what will "exist" in the "database" when you start the server.

The functions defined in `mockdb/mockdb_interface.py` are how you can query the mockdb. In `app.py`, where you will be writing your API, this has been imported with the name `db`. Therefore when you write the code for your endpoints, you can call the db interface functions like `db.get('users')`.

When you modify your code, the server will automatically update, _unless_ your code doesn't compile, in which case the server will stop running and you have to manually restart it after fixing your code.

## Part 1

Define the endpoint:

```
GET /users
```

This should return a properly formatted JSON response that contains a list of all the `user`s in the mockdb. If you call this endpoint immediately after starting the server, you should get this response in Postman:

```
{
  "code": 200,
  "message": "",
  "result": {
    "users": [
      {
        "age": 19,
        "id": 1,
        "name": "Aria",
        "team": "LWB"
      },
      {
        "age": 20,
        "id": 2,
        "name": "Tim",
        "team": "LWB"
      },
      {
        "age": 23,
        "id": 3,
        "name": "Varun",
        "team": "NNB"
      },
      {
        "age": 24,
        "id": 4,
        "name": "Alex",
        "team": "C2TC"
      }
    ]
  },
  "success": true
}
```

## Part 2

Define the endpoint:

```
GET /users/<id>
```

This should retrieve a single user that has the `id` provided from the request.

If there doesn't exist a user with the provided `id`, return a `404` with a descriptive `message`.

## Part 3

Extend the first `/users` enpoint by adding the ability to query the users based on the team they are on. You should _not_ use a url parameter like you did in Part 2. Instead, use a [query string](https://en.wikipedia.org/wiki/Query_string).

If `team` is provided as a query string parameter, only return the users that are in that team. If there are no users on the provided `team`, return an empty list.

For this exercise, you can ignore any query string parameters other than `team`.

In Postman, you can supply query string parameters in the `Params` section of request, doing so will automatically fill in the request url.

The following should happen

```
GET /users?team=LWB

{
  "code": 200,
  "message": "",
  "result": {
    "users": [{
      "age": 19,
      "id": 1,
      "name": "Aria",
      "team": "LWB"
    }, {
      "age": 20,
      "id": 2,
      "name": "Tim",
      "team": "LWB"
    }]
  },
  "success": true
}
```

## Part 4

Define the endpoint:

```
POST /users
```

This endpoint should create a new user. Each request should also send a `name`, `age`, and `team` parameter. The `id` property will be created automatically in the mockdb.

A successful request should return a status code of `201` and return the newly created user.

If any of the three required parameters aren't provided, DO NOT create a new user in the db and return a `422` with a useful `message`. In general, your messages should provide the user/developer useful feedback on what they did wrong and how they can fix it.

## Part 5

Define the endpoint:

```
PUT /users/<id>
```

Here we need to provide a user's `id` since we need to specify which user to update.

However, the difference with this `PUT` request is that only values with the provided keys (`name`, `age`, `team`) will be updated, and any parameters not provided will not change the corresponding attribute in the user being updated.

If the user with the provided `id` cannot be found, return a `404` and a useful `message`.

## Part 6

Define the endpoint:

```
DELETE /users/<id>
```

This will delete the user with the associated `id`. Return a useful `message`, although nothing needs to be specified in the response's `result`.

If the user with the provided `id` cannot be found, return a `404` and a useful `message`.

## Part 7 - Tests

Let's write unit tests! Unit tests are very important to software development. It enables to automatically check whether our functionality works or not since manually testing everything is very slow and error prone. Test Driven Development is a software development process in which we define a specification, write tests to that spec, then implement the functionality, and use the tests to validate whether it works. We've done a bit of that for you as the tests for Part 1-3 are written. To test them:

```
pipenv install --dev
pipenv run pytest
```

If your changes worked, you should see a green line saying `5 passed`. If they don't, follow the stack traces and fix your implementation. _Once they work, let's write tests for the Parts 3-6_.

We use [pytest](https://docs.pytest.org/en/latest/), a useful python test framework that automatically finds and runs python methods that start with `test`, such as `test_get_index`. In our case, we have a test file named `test_app.py`, which holds all the tests for Parts 1-3.

Each method also accepts a `client` object, which is automatically injected by pytest. `client` is a [test fixture](https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions), which is something that you may use in multiple tests, giving you a fixed baseline for your tests. When initializing, pytest looks into `conftest.py` and collects all fixtures. In our case, we have a `client` fixture, which gives a flask test client, which we can use to easily test our API. Look into how you can use the [Flask test client](http://flask.pocoo.org/docs/1.0/api/#test-client) to make other types of requests and how you can use the request payload.

## Submitting

When you're done with all the steps, push your changes to your github repo!

Let's run [black](https://github.com/ambv/black), a python formatter, before you submit. This removes all arguments on how we want to style your python code and gives reviewers a standardized style to review from.

From code directory run:

```
black .
```

Finally push your code to github, not directly on `master` branch but on the `dev` brach created in initail steps. Then create a pull request from dev branch and merge into master

Don't forget to share your postman workspace link in repo with properly named requests and sharing settings enabled
