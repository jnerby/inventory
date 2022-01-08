import os
import crud
import helpers
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
    all_inventory_items = crud.get_all_inventory_items()
    return render_template("base.html", all_inventory_items=all_inventory_items)


@app.route('/create', methods=['POST'])
def add_inventory_item():
    """Add a new inventory item to db"""
    if request.method == 'POST':
        product_name = request.form['product']
        qty = request.form['qty']

        # add new item to db
        crud.create_inventory_entry(qty, product_name)

    return redirect('/')

@app.route('/edit', methods=['POST'])
def edit_inventory_item():
    """Edit an existing inventory item in db"""
    if request.method == 'POST':
        to_edit = request.form['to_edit']
        to_edit_id = to_edit.split('|')[0].strip()

        edited_product_name = request.form['product']
        edited_qty = request.form['qty']

        crud.edit_entry(to_edit_id, edited_product_name, edited_qty)

    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_inventory_item():
    """Delete existing inventory item from"""
    if request.method == 'POST':
        to_edit = request.form['to_edit']
        to_edit_id = to_edit.split('|')[0].strip()

        crud.delete_entry(to_edit_id)

    return redirect('/')


@app.route('/report', methods=['POST'])
def generate_monthly_inventory_report():
    """Generates report for most in-stock items in a month/year"""
    if request.method == 'POST':
        # get month and year selected by user
        report_month_name = request.form['report-month']
        report_year = int(request.form['report-year'])

        # get month value from month name
        report_month = helpers.get_month_value(report_month_name)



        # get inventory items for requested month and year
        inventory_items = crud.get_inventory_by_month_year(report_month, report_year)
        
        helpers.generate_report_csv(inventory_items, report_month_name, report_year)

        # get 
        # product_counts = helpers.get_product_and_qty(inventory_items)

        # # create_dictionary_for_csv
        # sorted_product_counts = helpers.sort_inventory_by_count(product_counts)

        # max_min_in_stock = helpers.get_max_min_in_inventory(sorted_product_counts)


        # max = max_min_in_stock[0]
        # min = max_min_in_stock[1]



    return redirect('/')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 4444)))