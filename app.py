from flask import Flask, render_template, request, jsonify, send_from_directory
from database import load_games_from_db, getresult

app = Flask(__name__)
app.static = 'static'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        data = request.form
        users = getresult(data["search"])
    else:
        users = []
    print(users)

    return render_template("nextpage.html", usr=users)


@app.route("/api/games")
def list_games():
    games = load_games_from_db()
    return jsonify(games)


@app.route("/login")
@app.route("/search/login")
def login():
    return render_template("signin.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/video/Gamerok.mp4")
def intro_video():
    return render_template("intro_video.html",)

@app.route('/video/Gamerok.mp4')
def video(Gamerok):
    return send_from_directory(app.static, file=Gamerok.mp4)



if __name__ == "__main__":
    app.run('localhost', debug=True)