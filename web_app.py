from flask import Flask, request, jsonify
import db_connector

app = Flask(__name__)

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, the page you are looking for does not exist.", 404

@app.route('/stop_server', methods=['POST'])
def stop_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server stopped'

@app.route("/users/get_user_data/<user_id>")
def web_init(user_id):
    fetched_user = db_connector.readRecord(user_id)
    if not fetched_user["Success"]:
        return "<H1 id='error'>No such user " + user_id + "</H1>", 404  # Send a 404 status code

    return "<H1 id='user'>" + fetched_user["userName"] + "</H1>", 200  # Optionally, you can return a better response

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5001)
