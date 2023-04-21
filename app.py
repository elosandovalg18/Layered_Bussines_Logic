import os
from flask import Flask
import requests
from layer import movie_list, character_name_list


from flask import jsonify

print("Application startup")
port = int(os.environ.get("PORT", 8081))
print("PORT::", port)


app = Flask(__name__)

movie_url = "https://swapi.dev/api/films/"


@app.route("/", methods=['GET'])
def movie_list_endpoint():
    sorted_movies = movie_list()
    return jsonify(sorted_movies)

@app.route("/character_list/id_<int:movie_id>", methods=['GET'])
def character_name_list_endpoint(movie_id):
    character_names = character_name_list(movie_id)
    return jsonify(character_names)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)