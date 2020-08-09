import requests
from random import shuffle
API_TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTBjZDk4NTA3MjA1NzRhOGIzZDg3OTM1NTJjYjU5ZiIsInN1YiI6IjVmMjZhNzdlZTI2M2JiMDAzNTAzYjkxYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.T35Q1zXh8SFzllXf41kA8iwWDr8QvOZfFpkE-wdMAYM"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_name):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(path, size="w342"):
    base_url="https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{path}"

def get_movies(how_many,list_name='popular'):
    data=get_movies_list(list_name)['results']
    shuffle(data)
    return data[:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



