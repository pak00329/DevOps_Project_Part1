
from flask import Flask, request, jsonify
import db_connector
import os
import signal


app = Flask(__name__)

# accessed via <HOST>:<PORT>/get_random

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, the page you are looking for does not exist.", 404

if __name__ == '__main__':
    app.run()

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server_stopped'



@app.route("/user/<user_id>", methods=["POST", "GET", "PUT", "DELETE"])
def httpMethod(user_id):
    if request.method == "POST":
        return addUser(user_id)
    elif request.method == "GET":
        return retrieveUser(user_id)
    elif request.method == "PUT":
       return updateUser(user_id)
    elif request.method == "DELETE":
       return deleteUser(user_id)


def retrieveUser(user_id):
    result = db_connector.readRecord(user_id)
    if not result["Success"]:
        return jsonify(status="error", Reason="No such id"), 500
    return result["userName"]

    # return "test123"

def updateUser(user_id):
     userName = request.json.get("userName")
     result = db_connector.updateRecords(user_id, userName)
     if not result["Success"]:
         return jsonify(status="error", Reason="No such id"), 500
     return result["userName"]

def deleteUser(user_id):
    result = db_connector.deleteRecords(user_id)
    if not result["Success"]:
        return jsonify(status="error", Reason="No such id"), 500
    return result["userName"]

def addUser(user_id): # This function is to create the record

    userName = request.json.get("userName")  #this will extract from the post that has been sent
    db_connector.createRecords(user_id, userName)

    # return jsonify(status = "ok", user_added = userName), 200
    return jsonify(status="ok", user_added=[{"user_id": user_id,"userName":userName}]), 200


app.run(host='127.0.0.1', debug=True, port=5001)


