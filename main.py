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

@app.route('/finalScore', methods=["GET","POST"])
def finalScore():
    if request.method == "POST":
        subscription_key = "key"
        endpoint = "endpoint"
        sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"
        documents = {"documents": [
        {"id": "1", "language": "en",
        "text": request.form['content']},]}
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(sentiment_url, headers=headers, json=documents)
        sentiments = response.json()
        sentiment_overall = sentiments['documents'][0]['sentiment']
        confidences = sentiments['documents'][0]['confidenceScores']
        return jsonify({
            'sentiment': sentiment_overall,
            'confidences': confidences
        })
    return ""




