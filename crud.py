from model import db, Entry, Update, User
import datetime

def create_inventory_entry(qty, product_name):
    """Create inventory items"""
    new_entry = Entry(qty=qty, product_name=product_name, timestamp=datetime.datetime.now())
    db.session.add(new_entry)
    db.session.commit()

def get_product_obj_by_prod_name(product_name):
    """Returns product id from """

"""Edit inventory items"""

"""Delete inventory item(s)"""

"""View list of items"""