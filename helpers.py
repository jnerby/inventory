import os
import csv

def generate_report_csv(inventory_items, report_month_name, report_year):
    """Generates CSV report with all inventory entries for month and year"""
    path = os.getcwd()
    file_name = os.path.join(path, f"{report_month_name} {report_year} Inventory Report.csv")
    fieldnames = ['Product', 'Quantity', 'Timestamp']

    inventory_items_list = get_inventory_items_dict(inventory_items)

    try:
        with open(file_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for data in inventory_items_list:
                writer.writerow(data)
    except IOError:
        print('I/O Error')

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

    return product_counts

def create_dictionary_for_csv(product_counts):
    result = []
    for key, value in product_counts.items():
        inner_dict = {}
        inner_dict['Product'] = key
        inner_dict['Quantity'] = value
        result.append(inner_dict)

    return result

def get_inventory_items_dict(inventory_items):
    """Returns list with all inventory entries as dictionaries"""
    inventory_items_list = []
    for item in inventory_items:
        inner_dict = {}
        inner_dict['Product'] = item.product_name
        inner_dict['Quantity'] = item.qty
        inner_dict['Timestamp'] = item.timestamp
        inventory_items_list.append(inner_dict)

    return inventory_items_list

# def get_max_min_in_inventory(sorted_product_counts):
#     """Returns most in-stock item"""
#     # get list of sorted dict items
#     lst = list(sorted_product_counts.items())
#     max_in_stock = lst[0]
#     min_in_stock = lst[-1]

#     return (max_in_stock, min_in_stock)


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
