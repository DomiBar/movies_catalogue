import requests
from random import shuffle
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")


def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_popular_movies():
    return call_tmdb_api(f"movie/popular")


def get_movies_list(list_name):
    return call_tmdb_api(f"movie/{list_name}")


def get_poster_url(path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{path}"


def get_movies(how_many, list_name='popular'):
    data = get_movies_list(list_name)['results']
    shuffle(data)
    return data[:how_many]


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]


def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")
