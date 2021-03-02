import pickle

from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, request, jsonify
from config import FEATURE_EXTRACTOR_FILEPATH, CLASSIFIER_FILEPATH, LABELS

app = Flask(__name__)

with open(FEATURE_EXTRACTOR_FILEPATH, 'rb') as infile:
    app.feature_extractor = pickle.load(infile)

with open(CLASSIFIER_FILEPATH, 'rb') as infile:
    app.classifier = pickle.load(infile)

def reply_success(data):
    response = jsonify({
        "data": data
    })

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

def reply_error(code, message):
    response = jsonify({
        "error": {
            "code": code,
            "message": message
        }
    })

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route("/")
def index():
    return "<h1>Sentiment Analysis API using Flask</h1>"

@app.route("/classify", methods=["GET", "POST"])
def classify():
    if request.method == "GET":
        text = request.args.get("text", None)
    elif request.method == "POST":
        json_req = request.get_json()
        text = json_req["text"]
    else:
        return reply_error(code=400, message="Supported method is 'GET' and 'POST'")

    if text:
        # IMPORTANT: Use [text] because sklearn vectorizer expects an iterable as the input
        # IMPORTANT: classifier.predict returns an array, so get the first element
        label = app.classifier.predict(app.feature_extractor.transform([text]))[0]

        return reply_success(data={
            'text': text,
            'sentiment': LABELS[label]
        })

    return reply_error(code=400, message="Text is not specified")

if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    port = int(environ.get("PORT"))
    debug = environ.get("DEBUG")

    if debug == "True":
        app.run(threaded=True, port=port, debug=True)
    else:
        app.run(threaded=True, port=port, debug=False)
