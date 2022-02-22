# from crypt import methods
#from crypt import methods
from typing import Tuple
from flask import request
from urllib.parse import urlparse
from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.

    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if data is None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/users")
def users():
    data = db.get("users")
    return create_response(data)

@app.route("/users/<id>")
def spid(id):
    data = db.getById("users", int(id))
    return create_response(data)

@app.route("/users/teams")
def users_query():
    var = request.args.get("team")
    print(var)
    data = db.get("users")
    temp=[]
    for user in data:
        if user['team'] == var:
            temp.append(user)
    return create_response(temp)

@app.route("/createuser", methods = ['POST'])
def createuser():
    temp = request.json
    data = db.create("users",temp)
    return create_response(data)

@app.route("/users/<id>", methods = ['PUT'])
def update(id):
    temp = request.json
    data = db.updateById("users", int(id),temp)
    if data is None:
        return ({"status": 404, "message":"User not found"})
    return create_response(data)

@app.route("/users/<id>", methods = ['DELETE'])
def delete(id):
    db.deleteById("users", int(id)) is not None
    if db.get("users") is not None:
        return {"status": 200, "message":"User Deleted Successfully"}
    else:
        return {"status": 404, "message":"Unsuccessfully"}

# TODO: Implement the rest of the API here!

    """
    ~~~~~~~~~~~~ END API ~~~~~~~~~~~~
    """
if __name__ == "__main__":
    app.run(debug=True)
