import tmdb_client
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path)
    # Porównanie wyników
    assert expected_default_size in poster_url


def test_call_tmdb_api(monkeypatch):
    full_url_mock = f"website"

    requsts_mock = Mock()
    response = requsts_mock.return_value
    response.json.return_value = full_url_mock
    monkeypatch.setattr("tmdb_client.requests.get", requsts_mock)

    full_url = tmdb_client.call_tmdb_api(f"none")
    assert full_url == full_url_mock


def test_get_movies_list():
    movies_list = tmdb_client.get_movies_list("popular")
    assert movies_list is not None


def test_get_single_movie():
    movie = tmdb_client.get_single_movie(547016)
    assert movie is not None


def test_get_movie_images():
    movie = tmdb_client.get_movie_images(547016)
    assert movie is not None


def test_get_single_movie_cast():
    movie = tmdb_client.get_single_movie_cast(547016)
    assert movie is not None
