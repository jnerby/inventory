from model import db, Entry
import datetime

def create_inventory_entry(qty, product_name):
    """Create inventory items"""
    new_entry = Entry(qty=qty, product_name=product_name, timestamp=datetime.datetime.now())
    db.session.add(new_entry)
    db.session.commit()


# def edit_inventory_item_product_name(to_edit_id, edited_product_name):
#     """Edit inventory item"""
#     # get entry user wants to edit
#     entry_to_edit = Entry.query.filter(Entry.entry_id==to_edit_id).first()

#     # update product name and timestamp
#     entry_to_edit.product_name = edited_product_name
#     entry_to_edit.timestamp = datetime.datetime.now()

#     # add and commit to db
#     db.session.add(entry_to_edit)
#     db.session.commit()

#     return entry_to_edit

# def edit_inventory_item_qty(to_edit_id, edited_qty):
#     """Edit inventory item"""
#     # get entry user wants to edit
#     entry_to_edit = Entry.query.filter(Entry.entry_id==to_edit_id).first()

#     # update quantity and timestamp
#     entry_to_edit.qty = edited_qty
#     entry_to_edit.timestamp = datetime.datetime.now()

#     db.session.add(entry_to_edit)
#     db.session.commit()

#     return entry_to_edit

def delete_entry(to_delete_id):
    """Delete inventory entry"""
    entry_to_delete = Entry.query.filter(Entry.entry_id==to_delete_id).first()
    db.session.delete(entry_to_delete)
    db.session.commit()


def edit_entry(to_edit_id, edited_product_name, edited_qty):
    """Edit inventory entry"""
    entry_to_edit = Entry.query.filter(Entry.entry_id==to_edit_id).first()

    if edited_product_name is not "":
        # get entry user wants to edit
        entry_to_edit.product_name = edited_product_name
    if edited_qty is not "":
        entry_to_edit.qty = int(edited_qty)

    
    db.session.add(entry_to_edit)
    db.session.commit()

    return entry_to_edit 


"""Delete inventory item(s)"""

def get_all_inventory_items():
    """Returns all entry objects"""
    return Entry.query.all()
