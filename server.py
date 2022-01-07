import os
import crud
from flask import flash, Flask, jsonify, redirect, render_template, request
from jinja2 import StrictUndefined
from model import db, connect_to_db

app = Flask(__name__)
app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/')
def render_homepage():
    """Render homepage"""
    return render_template('base.html')

@app.route('/create', methods=['POST'])
def add_inventory_item():
    """Add a new inventory item to db"""
    if request.method == 'POST':
        product_name = request.form['product']
        qty = request.form['qty']

        # add new item to db
        crud.create_inventory_entry(qty, product_name)

    return redirect('/')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 4444)))