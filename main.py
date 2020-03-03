from flask import Flask, render_template, jsonify, request
from Analyze import score as score_text
from base64 import b64decode as b64d
app = Flask(__name__)

app.secret_key = b'_5#y2gyhsghyttryrthgfjkjutrtqtregdfgdL"F4Q8z\n\asdasdasdas]/'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/score', methods=["GET","POST"])
def score():
    if request.method == "POST":

        content = request.form['content']
        avg, good, bad = score_text(content)

        return jsonify({
            'score': avg,
            'good': good,
            'bad': bad
        })
    return False

