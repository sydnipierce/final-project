from flask import Flask, render_template, jsonify, request, redirect

import os
import numpy as np
import pandas as pd
from urllib.request import urlopen
import cloudpickle as cp

from wordcloud import WordCloud


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    wc = WordCloud()
    # img = wc.generate_from_text(' '.join(tokenized_word_2))
    # img.to_file('worcloud.jpeg')

    loaded_model = cp.load(urlopen("https://butlerunit22.s3.us-east-2.amazonaws.com/class_model.sav", 'rb'))
    print(loaded_model)
    user_input = request.form["variable"]
    print(user_input)
    if request.method == "POST":
        result = loaded_model.score(user_input)
        print(result)
    return render_template("index.html", results=result)

if __name__ == "__main__":
    app.run(debug=True)