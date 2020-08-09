from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route('/')
def homepage():
    list_array=['popular','now_playing','top_rated','upcoming']
    selected_list=request.args.get('list_type', "popular")
    if selected_list in list_array:
        pass
    else:
        selected_list='popular'
    movies = tmdb_client.get_movies(10, list_name=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, list_array=list_array)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)[:8]
    images = tmdb_client.get_movie_images(movie_id)
    random_image=random.choice(images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, image=random_image)


if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.run(debug=True)
