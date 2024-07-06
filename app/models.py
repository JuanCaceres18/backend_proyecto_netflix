# Representación de las estructuras con las que trabaja mi app

from app.database import get_db

class Movie:
    # Inicializar instancia de Movie
    def __init__(self, id_movie = None, title=None, director = None, score = None, release_date = None, banner = None):
        self.id_movie = id_movie
        self.title = title
        self.director = director
        self.score = score
        self.release_date = release_date
        self.banner = banner
    
    # Método para obtener el listado de películas
    @staticmethod
    def get_all_movies():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()
        movies = [Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], score=row[4], banner=row[5]) for row in rows]
        cursor.close()
        return movies
              
    # Método para obtener una única película a través del id
    @staticmethod
    def get_movie(id_movie):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies WHERE id_movies=%s",(id_movie,))
        row = cursor.fetchone()
        if (row):
            return Movie(id_movie=row[0], title=row[1], director=row[2],
                         release_date=row[3], score=row[4],banner=row[5])
        return None

    # Método para guardar/actualizar una película
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_movie:
            cursor.execute("""
                UPDATE movies SET title=%s, director=%s, release_date=%s,score=%s, banner=%s WHERE id_movies=%s
                           """,(self.title, self.director, self.release_date, self.score, self.banner, self.id_movie))
        else:
            cursor.execute("""
                    INSERT INTO movies(title, director, release_date, score, banner) VALUES (%s, %s, %s, %s, %s)
                           """, (self.title, self.director, self.release_date, self.score, self.banner))
            self.id_movie = cursor.lastrowid
        db.commit()
        cursor.close()

    # Método para eliminar películas
    def delete_movie(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM movies WHERE id_movies = %s", (self.id_movie,))
        db.commit()
        cursor.close()

    # Método para convertir objeto Movie en diccionario
    def serialize(self):
        return {
            "id_movies":self.id_movie,
            "title":self.title,
            "director":self.director,
            "release_date":self.release_date,
            "score":self.score,
            "banner":self.banner
        }