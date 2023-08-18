from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Домашняя страница
    return render_template('home.html')

if __name__ == "__main__":
    app.run("0.0.0.0")
