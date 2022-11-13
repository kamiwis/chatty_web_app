# from threading import Lock
from flask import Flask, render_template, session, redirect, request, url_for, jsonify, flash
from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
Bootstrap(app)


@app.route('/')
@app.route('/home')
def index():
    """
    Displays chat if user is logged in.
    """
    if 'NAME' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', name=session["NAME"],  **{"session": session})


# @app.route("/chat", methods=["GET", "POST"])
# def view_chat():
#     return render_template("chat_app.html", name=session["NAME"])

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Renders login page to save user's name for chat session.
    """
    if request.method == "POST":
        name = request.form["username"]
        session["NAME"] = name
        flash(f"You are signed in as {name}")
        return redirect(url_for("index"))

    return render_template("login.html", **{"session": session})

@app.route("/logout")
def logout():
    """
    logs the user out by popping name from session
    :return: None
    """
    session.pop("NAME", None)
    flash("You were logged out.")
    return redirect(url_for("login"))


def message_received(msg, methods=["GET", "POST"]):
    print('Message was received!')


@socketio.on('my event')
def handle_message(json, methods=["GET", "POST"]):
    print('Received event: ' + str(json))
    emit('my response', json, broadcast=True, callback=message_received)


@app.route("/get_name")
def get_name():
    """
    :return: a json object storing name of logged in user
    """
    data = {"name": ""}
    if "NAME" in session:
        data = {"name": session["NAME"]}
    return jsonify(data)


if __name__ == '__main__':
    socketio.run(app, host="192.168.1.68", port=5000)
