from flask import Flask, render_template, request, jsonify, send_from_directory
from database import load_games_from_db, getresult
import sys
import os
import requests

app = Flask(__name__)
app.static = 'static'
app.secret_key = '1234567890'


@app.route("/")
def index():
    return render_template("index.html")

users=[]
@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        data = request.form
        users = getresult(data["search"])
    # else:
    #     users = "Sorry!! Either is not updated in the list or wrong spelling Please wait until next time for the game to be updated in the list."
    # print(users)
    return render_template("nextpage.html", usr=users)

print(users)

@app.route("/api/games")
def list_games():
    games = load_games_from_db()
    return jsonify(games)


@app.route("/login")
@app.route("/search#/login")
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
    return render_template("intro_video.html")


@app.route('/video/Gamerok.mp4')
def video(Gamerok):
    return send_from_directory(app.static, file=Gamerok.mp4)


@app.route("/image", methods=['GET', 'POST'])
# def image():
#     searchResult = ''
#     message = ''
#     searchQuery = ''
#     clientId = 'y4i-BtdyHO0mBSE7BhqVPgCBFhqbaTtruS9oZmyKMho'
#     if request.method == 'POST':
#         searchQuery = str(request.form['searchQuery'])
#         if searchQuery:
#             apiUrl = 'https://api.unsplash.com/search/photos'
#             params = {'query': searchQuery, 'client_id': clientId}
#             response = requests.get(apiUrl, params=params, allow_redirects=True)
#             searchResult = response.json()
#         else:
#             message = 'Please enter search keyword'
#     return render_template('image.html', message=message, searchQuery=searchQuery, searchResult=searchResult)

def image():
    url = "https://rawg-video-games-database.p.rapidapi.com/games"
    headers = {
        "X-RapidAPI-Key": "3473346827msh600c8fbfd42e64ep1c5334jsn90f3782fb178",
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com/users"
    }

    response = requests.get(url, headers=headers)

    return render_template("image.html", image=response.json())

if __name__ == "__main__":
    app.run('localhost', debug=True)
