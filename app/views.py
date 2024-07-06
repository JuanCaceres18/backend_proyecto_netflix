# Manejan las solicitudes HTTPS y brindan una respuesta adecuada

from flask import jsonify, request
from app.models import Movie

def index():
    return jsonify({"message":"Hola desde Flask"})

# Función para obtener todas las películas
def get_all_movies():
    movies = Movie.get_all_movies()
    return jsonify([movie.serialize() for movie in movies])

# Función para obtener una película
def get_movie(id_movie):
    movie = Movie.get_movie(id_movie)
    if not movie:
        return jsonify({"message":"Movie not found"}), 404
    return jsonify(movie.serialize())

# Función para guardar/actualizar una película
def create_movie():
    data = request.json
    new_movie = Movie(title=data["title"], director=data["director"],
                      release_date=data["release_date"], score=data["score"],
                      banner=data["banner"])
    new_movie.save()
    return jsonify({"message":"Movie created successfully!", "data": data}), 201

# Función para actualizar una película
def update_movie(id_movie):
    movie = Movie.get_movie(id_movie)
    if not movie:
        return jsonify({"message":"Movie not found"}),404
    data = request.json
    movie.title = data["title"]
    movie.director = data["director"]
    movie.release_date = data["release_date"]
    movie.score = data["score"]
    movie.banner = data["banner"]
    movie.save()
    return jsonify({"message":"Movie updated successfully!"})

# Función para eliminar una película
def delete_movie(id_movie):
    movie = Movie.get_movie(id_movie)
    if not movie:
        return jsonify({"message":"Movie not found"}), 404
    movie.delete_movie()
    return jsonify({"message":"Movie deleted successfully!", "id_movie":id_movie})

