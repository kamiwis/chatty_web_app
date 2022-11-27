from flask import Flask, render_template, session, redirect, request, url_for,\
    jsonify
from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap

# Create and configure app
app = Flask(__name__)
app = Flask(__name__, instance_relative_config=None)
app.config.from_object('config.Config')

# Create socketio instance
socketio = SocketIO(app, cors_allowed_origins="*")
# Load Bootstrap
Bootstrap(app)


@app.route('/')
@app.route('/home')
def index():
    """
    Displays chat if user is logged in.
    """
    if 'NAME' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', name=session["NAME"],
                           **{"session": session})


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Renders login page to save user's name for chat session.
    """
    if request.method == "POST":
        name = request.form["username"]
        session["NAME"] = name
        return redirect(url_for("index"))

    return render_template("login.html", **{"session": session})


@app.route("/logout")
def logout():
    """
    Logs the user out by popping name from session.
    """
    session.pop("NAME", None)
    return redirect(url_for("login"))


@socketio.on('my event')
def handle_message(json, methods=["GET", "POST"]):
    print('Received event: ' + str(json))
    emit('my response', json, broadcast=True)


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
    socketio.run(app, host="localhost", port=5000)
