import requests
from random import shuffle


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTBjZDk4NTA3MjA1NzRhOGIzZDg3OTM1NTJjYjU5ZiIsInN1YiI6IjVmMjZhNzdlZTI2M2JiMDAzNTAzYjkxYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.T35Q1zXh8SFzllXf41kA8iwWDr8QvOZfFpkE-wdMAYM"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(path, size="w342"):
    base_url="https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{path}"

def get_movies(how_many):
    data=get_popular_movies()['results']
    shuffle(data)
    return data[:how_many]
