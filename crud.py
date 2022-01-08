from model import db, Entry
from sqlalchemy import extract
import datetime

def create_inventory_entry(qty, product_name):
    """Create inventory items"""
    new_entry = Entry(qty=qty, product_name=product_name, timestamp=datetime.datetime.now())
    db.session.add(new_entry)
    db.session.commit()

    return new_entry


def delete_entry(to_delete_id):
    """Delete inventory entry"""
    entry_to_delete = Entry.query.filter(Entry.entry_id==to_delete_id).first()
    db.session.delete(entry_to_delete)
    db.session.commit()

    return "Deleted"


def edit_entry(to_edit_id, edited_product_name, edited_qty):
    """Edit inventory entry"""
    entry_to_edit = Entry.query.filter(Entry.entry_id==to_edit_id).first()

    if edited_product_name != "":
        # get entry user wants to edit
        entry_to_edit.product_name = edited_product_name
    if edited_qty != "":
        entry_to_edit.qty = int(edited_qty)
    
    db.session.add(entry_to_edit)
    db.session.commit()

    return entry_to_edit 


def get_all_inventory_items():
    """Returns all entry objects"""
    return Entry.query.all()


def get_inventory_by_month_year(report_month, report_year):
    """Return all inventory for a given month and year"""
    inventory_items = Entry.query.filter((extract('month', Entry.timestamp)==report_month) & ((extract('year', Entry.timestamp)==report_year))).all()
    return inventory_items
