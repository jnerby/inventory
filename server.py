import os
from flask import flash, Flask, jsonify, redirect, render_template, request

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def render_homepage():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 4444)))