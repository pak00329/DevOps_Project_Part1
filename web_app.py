
from flask import Flask, request, jsonify
import db_connector


app = Flask(__name__)

@app.route("/users/get_user_data/<user_id>")
def web_init(user_id):
    fetched_user = db_connector.readRecord(user_id)
    if not fetched_user["Success"]:
        return "<H1 id = 'error'> no such user " + user_id + "</H1>"


    return "<H1 id = 'user'>" + fetched_user["userName"] + "</H1>"

app.run(host='127.0.0.1', debug=True, port=5001)


