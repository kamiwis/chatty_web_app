from flask import Flask, render_template, url_for, session, request, redirect
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, emit
import config


# Create and configure app.
app = Flask(__name__, instance_relative_config=None)
app.config.from_object('config.Config')
Bootstrap(app)

# Create socketio instance.
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


def message_received(methods=["GET", "POST"]):
    print('Message was received.')


# Listen for message event.
@socketio.on('my event')
def handleMessage(json, methods=["GET", "POST"]):
    print('Received event: ' + str(json))
    emit('my response', json, callback=message_received)


# @socketio.on('event')
# def handle_message(json):
#     # Print received message.
#     print('Received json: ' + str(json))
#     # Send message to all connected users.
#     emit('message response', json)


# @app.route("/", methods=["GET", "POST"])
# def login():
#     """
#     Renders login page to save user's name for chat session.
#     """
#     if request.method == "POST":
#         session["NAME"] = request.form["username"]
#         return redirect(url_for("view_chat"))

#     return render_template("login.html")

# @app.route("/chat", methods=["GET", "POST"])
# def view_chat():

#     return render_template("chat_app.html", name=session["NAME"])

if __name__ == "__main__":
    socketio.run(app, host='localhost')
