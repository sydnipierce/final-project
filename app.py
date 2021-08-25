from flask import Flask, render_template, jsonify, request, redirect

import os
import numpy as np
import pandas as pd
from urllib.request import urlopen
# import cloudpickle as cp

# from wordcloud import WordCloud
# methods=["GET", "POST"]

app = Flask(__name__)
from urllib.request import urlopen
from sklearn.externals import joblib
Nu_SVC_classifier = joblib.load(urlopen("https://butlerunit22.s3.us-east-2.amazonaws.com/class_model.sav"))
# loaded_model = cp.load(urlopen("https://butlerunit22.s3.us-east-2.amazonaws.com/class_model.sav", 'rb'))


@app.route('/')
def home():
    # wc = WordCloud()
    # img = wc.generate_from_text(' '.join(tokenized_word_2))
    # img.to_file('worcloud.jpeg')
    return render_template("index.html")

@app.route('/send', methods=["GET", "POST"])
def submit():
    
    # print(type(loaded_model))
    if request.method == "POST":
        user_input = []
        text_input = request.form["variable"]
        user_input.append(text_input)
        print(user_input)
        # result = user_input
        result = Nu_SVC_classifier.predict(user_input)
        print(result)

    return render_template("index.html")

    # , results=result

if __name__ == "__main__":
    app.run(debug=True)