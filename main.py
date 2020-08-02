from flask import Flask, render_tempalte

app = Flask(__name__)

@app.route('/')
def hompage():
    return render_tempalte("index.html")

if __name__ == "__main__":
    app.run(debug=True)