from flask import Flask, request, jsonify, make_response
import db_connector

app = Flask(__name__)

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, the page you are looking for does not exist.", 404

@app.errorhandler(Exception)
def handle_exception(e):
    return make_response(jsonify(error=str(e)), 500)

@app.route("/users/<user_id>", methods=["POST", "GET", "PUT", "DELETE"])
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
        return jsonify(status="error", Reason="No such id"), 404
    return jsonify(userName=result["user_name"]), 200

def updateUser(user_id):
    userName = request.json.get("user_name")
    result = db_connector.updateRecords(user_id, userName)
    if not result["Success"]:
        return jsonify(status="error", Reason="No such id"), 404
    return jsonify(userName=result["user_name"]), 200

def deleteUser(user_id):
    result = db_connector.deleteRecords(user_id)
    if not result["Success"]:
        return jsonify(status="error", Reason="No such id"), 404
    return jsonify(userName=result["user_name"]), 200

def addUser(user_id):
    userName = request.json.get("user_name")
    db_connector.createRecords(user_id, userName)
    return jsonify(status="ok", user_added={"user_id": user_id, "user_name": userName}), 201

@app.route('/stop_server', methods=['POST'])
def stop_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server stopping...'

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
