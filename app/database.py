# Manejo de configuración y conexión a base de datos

import os
import mysql.connector
from flask import g
from dotenv import load_dotenv

# Cargo las variables de entorno (.env)
load_dotenv()

# Configuración de la base de datos
DATABASE_CONFIG = {
    "user":os.getenv("DB_USERNAME"),
    "host":os.getenv("DB_HOST"),
    "password":os.getenv("DB_PASSWORD"),
    "port":os.getenv("DB_PORT",3306), # Si la variable no está definida, proporciono un valor por defecto
    "database":os.getenv("DB_NAME")
}

# Función para obtener conexión a la base de datos
def get_db():
    # Si db no está en el contexto global de g...
    if "db" not in g:
        # Creo conexión a base de datos
        g.db = mysql.connector.connect(**DATABASE_CONFIG) # Desempaquetado
    return g.db

# Función para cerrar la base de datos
def close_db(e=None):
    db = g.pop("db", None) # Extraigo conexión a la base de datos y la elimino
    if db is not None: # Si la base de datos ya existe, la cierro
        db.close()

# Función para inicializar la app con el manejo de la base de datos
def init_app(app):
    # Registrar close_db para que se ejecute al final del contexto de la app
    app.teardown_appcontext(close_db)