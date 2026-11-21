import csv 
import os
import json
from flask import Flask, request

app = Flask(__name__)

CSV_FILENAME = os.environ.get("MOVIES_CSV", "imdb-movie-data.csv")

def load_movies(csv_path):
    if not os.path.exists(csv_path):
        return []
    
    movies = []
    with open(csv_path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies = movies + [dict(row)]
    return movies

MOVIES = load_movies(CSV_FILENAME)
print('Nombre de film : ',len(MOVIES))
print('Premier film : ',MOVIES[0] if MOVIES else 'Acun film trouve')

def filter_by_genre(movies_list, genre_query):
    if not genre_query:
        return movies_list
    
    target = genre_query.strip().lower()
    filtered = []

    for movie in movies_list:
        raw_genre = movie.get("Genre") or ""
        genres = [g.strip().lower() for g in raw_genre.split(",") if g.strip()]
        if target in genres :
            filtered = filtered + [movie]
    return filtered  

@app.route("/", methods=["GET"])
def index():
    genre = request.args.get('genre')
    results = filter_by_genre(MOVIES, genre)
    return json.dumps(results)
@app.route("/action", methods=["GET"])
def get_action():
    return json.dumps(filter_by_genre(MOVIES, "action"))

@app.route("/adventure", methods=["GET"])
def get_adventure():
    return json.dumps(filter_by_genre(MOVIES, "adventure"))

@app.route("/comedy", methods=["GET"])
def get_comedy():
    return json.dumps(filter_by_genre(MOVIES, "comedy"))

@app.route("/drama", methods=["GET"])
def get_drama():
    return json.dumps(filter_by_genre(MOVIES, "drama"))

@app.route("/romance", methods=["GET"])
def get_romance():
    return json.dumps(filter_by_genre(MOVIES, "romance"))

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=False)