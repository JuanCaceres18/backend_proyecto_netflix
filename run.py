from flask import Flask
from app.views import *
from app.database import init_app

# Creo la aplicación Flask
app = Flask(__name__)

# Conecto la app con la base de datos
init_app(app)

# Prueba de solicitud GET
app.route("/", methods=["GET"])(index)

# Ruta 1 - Obtener películas
app.route("/api/movies/", methods=["GET"])(get_all_movies)

# Ruta 2 - Obtener una película por id
app.route("/api/movies/<int:id_movie>", methods=["GET"])(get_movie)

# Ruta 3 - Crear película
app.route("/api/movies/", methods=["POST"])(create_movie)

# Ruta 4 - Editar película
app.route("/api/movies/<int:id_movie>", methods=["PUT"])(update_movie)

# Ruta 5 - Eliminar película
app.route("/api/movies/<int:id_movie>", methods=["DELETE"])(delete_movie)


if __name__ == "__main__":
    app.run(debug=True)