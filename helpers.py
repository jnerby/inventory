import os
import csv


def generate_dict_for_csv(inventory_items):
    """Returns list of dictionaries with total qty per product to populate csv"""
    list_of_dicts = []

    # get total qty per product sorted from max to min
    product_qty = get_product_and_qty(inventory_items)

    # add each dictionary to list of dicts with product and quantity keys
    for key, value in product_qty.items():
        inner_dict = {}
        
        inner_dict['Product'] = key
        inner_dict['Quantity'] = value

        list_of_dicts.append(inner_dict)
    
    return list_of_dicts


def generate_report_csv(inventory_items, report_month_name, report_year):
    """Generates CSV report with all inventory entries for month and year"""
    # set path to current working dictionary
    path = os.getcwd()
    file_name = os.path.join(path, f"{report_month_name} {report_year} Inventory Report.csv")
    fieldnames = ['Product', 'Quantity']

    # get dict of products and quantities sorted by quantity
    inventory_items_list = generate_dict_for_csv(inventory_items)

    try:
        with open(file_name, 'w') as csv_file:
            # add headers to csv
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            # add each product and quantity as rows to csv
            for data in inventory_items_list:
                writer.writerow(data)
    except IOError:
        print('I/O Error')


def get_entry_id_from_string(to_update):
    """Return id of """
    return to_update.split('|')[0].strip()


def get_product_and_qty(inventory_items):
    """Returns dictionary with counts of each item in inventory"""
    product_counts = {}

    for item in inventory_items:
        product_name = item.product_name
        product_qty = item.qty

        if product_name in product_counts:
            product_counts[product_name] += product_qty
        else:
            product_counts[product_name] = product_qty

    # return dict of product counts sorted from max to min
    return sort_inventory_by_count(product_counts)


def get_month_value(report_month_name):
    """Returns numerical value of report month user entered"""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November','December']

    # get month value from month name
    report_month = months.index(report_month_name) + 1

    return report_month


def sort_inventory_by_count(product_counts):
    """Sorts inventory dictionary desc by count"""
    return dict(sorted(product_counts.items(), key=lambda item: item[1], reverse=True))
