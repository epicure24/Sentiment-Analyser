import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pickle

from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sentiment_analyzer import sentiment_analyzer

"""
Loading the trained model and tokenizer
"""
model = load_model('model/model_loss_0.274_acc_0.88807.h5')

with open('model/tokenizer_loss_0.274_acc_0.888.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

app = Flask(__name__)

"""
API to detect the sentiment
"""
@app.route('/api/detect', methods=['POST'])
def detect():
    try:
        review = request.form['review']
        score, sentiment = sentiment_analyzer(review, model, tokenizer)
        return jsonify({
                            "status":{
                                "responseStatus":"success",
                                },
                            "desc":"Sentiment Analysis of the review",
                            "result": {
                                "sentiment": sentiment,
                                "score": str(score)
                            }}),200
    except:
        return jsonify({"status":{
                        "responseStatus":"fail"
                        },
                "desc":"An error occured in detecting sentiment.",
                'result': 'unsuccessful'}),422


"""
Routes that renders HTML screens
"""
@app.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template('index.html')

"""
Result route to show the sentiment
"""
@app.route('/detect', methods=['POST'])
def result_page():
    review = request.form['review']
    score, sentiment = sentiment_analyzer(review, model, tokenizer)
    if sentiment == 'NEGATIVE':
        color = 'red'
    else:
        color = 'green'
    return render_template('result.html', 
                            score=score, 
                            sentiment=sentiment,
                            review = review,
                            color=color
                            )



if __name__ == '__main__':
    app.run()
