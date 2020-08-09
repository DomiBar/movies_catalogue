from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def hompage():
    movies=tmdb_client.get_movies(10)
    return render_template("hompage.html", movies=movies)


if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.run(debug=True)
