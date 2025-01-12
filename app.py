from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/word-puzzle')
def word_puzzle():
    return render_template('puzzle-game.html')


@app.route('/bubble-shooter')
def bubble_shooter():
    return render_template('bubble-shooter.html')


@app.route('/sliding-puzzle')
def sliding_puzzle():
    return render_template('sliding-puzzle.html')


if __name__ == '__main__':
    app.run(debug=True)
