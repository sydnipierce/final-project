from flask import Flask, render_template, jsonify, request, redirect

import os
import numpy as np
import pandas as pd
import pickle


app = Flask(__name__)

@app.route('/', methods=["POST"])
def home():
    model = os.path.join("Data", "model.sav")
    loaded_model = pickle.load(open(model, 'rb'))

    if request.method == "POST":
        user_input = request.form['variable']
        result = loaded_model.score(user_input)
        print(result)

    return render_template("index.html", results=result)

if __name__ == "__main__":
    app.run(debug=True)