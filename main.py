from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hompage():
    movies=[]
    for i in range(10):
        movies.append(i)
    return render_template("hompage.html", movies=movies)


if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.run(debug=True)
