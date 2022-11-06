# from threading import Lock
from flask import Flask, render_template, session, redirect, request, url_for
from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if 'NAME' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('view_chat'))


@app.route("/chat", methods=["GET", "POST"])
def view_chat():
    return render_template("chat_app.html", name=session["NAME"])

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Renders login page to save user's name for chat session.
    """
    if request.method == "POST":
        session["NAME"] = request.form["username"]
        return redirect(url_for("view_chat"))

    return render_template("login.html")


def message_received(msg, methods=["GET", "POST"]):
    print('Message was received!')


@socketio.on('my event')
def handle_message(json, methods=["GET", "POST"]):
    print('Received event: ' + str(json))
    emit('my response', json, broadcast=True, callback=message_received)


if __name__ == '__main__':
    socketio.run(app, debug=True)
