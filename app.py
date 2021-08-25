from flask import Flask, render_template, jsonify, request, redirect

import os
import numpy as np
import pandas as pd
from urllib.request import urlopen
import cloudpickle as cp

# from wordcloud import WordCloud
# methods=["GET", "POST"]

app = Flask(__name__)
# from urllib.request import urlopen
# import joblib
# model = joblib.load(urlopen("https://drive.google.com/file/d/1y03andRphelw4zxhIswwIkjDyEu6T8um/view?usp=sharing"))

#loaded_model = cp.load('pickle_model.sav')

# model = cp.load(urlopen("https://butlerunit22.s3.us-east-2.amazonaws.com/pickel_model.sav", 'rb'))
# model = cp.load(urlopen("https://butlerunit22.s3.us-east-2.amazonaws.com/pickel_model.sav"))


with open('pickle_model.sav', mode='rb') as file:
    model = cp.load(file)

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
        coded_result = model.predict(user_input)
        if (coded_result == [0]):
            result = "FAKE"
        else:
            result = "TRUE"
        print(result)

    return render_template("index.html", results=result)

    # , results=result

if __name__ == "__main__":
    app.run(debug=True)