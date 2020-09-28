from flask import Flask, session, render_template, jsonify, request
from Analyze import score as score_text
from base64 import b64decode as b64d
app = Flask(__name__)

app.secret_key = b'_5#y2gyhsghyttryrthgfjkjutrtqtregdfgdL"F4Q8z\n\asdasdasdas]/'

@app.route('/')
def index():
    if session.get('text') is None:
        session['text'] = ""
        session['last_response']=""
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
        text = request.form['content']
        if(text == session.get('text'):
           return session.get('last_response')
        subscription_key = "key"
        endpoint = "endpoint"
        sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"
        documents = {"documents": [
        {"id": "1", "language": "en",
        "text": text},]}
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(sentiment_url, headers=headers, json=documents)
        sentiments = response.json()
        session['text'] = text
        session['last_response'] = sentiments
        return sentiments
        
    return ""




