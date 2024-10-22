# inventory_system.py

import numpy as np
from copy import deepcopy


def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    inv = {
        'Electronics': {
            'Laptop': {'name': 'Laptop', "price": 2500 ,'quantity': 5} 
        },
        'Groceries': {}
    }
    return inv

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    if item_name not in inventory[category]:
        inventory[category][item_name] = {}
    
    for key, value in update_info.items():
        inventory[category][item_name][key] = value
    
    return inventory

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    # Step 1 : Create a copy of inv1 
    merged_inv = {
        cat: {
            item: data.copy()
            for item, data in items.items()
        }
        for cat, items in inv1.items()
    }
    
    # Step 2:
    for cat, items in inv2.items():
        # If key not already available in merged_inv, create a new key
        if cat not in merged_inv:
            merged_inv[cat] = {}
        
        # Else, if there is a common key across inv1 and inv2, add up the quantities for the same category and item.
        for item, data in items.items():
            # for all the keys inside the nested dict, sum up the quantity.
            if item in merged_inv.get(cat, {}):
                merged_inv[cat][item]['quantity'] = merged_inv[cat][item].get("quantity", 0) + data.get("quantity", 0)
            else:
                merged_inv[cat][item] = data.copy()
    
    return merged_inv
            
        

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory[category]

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    max_price = -np.inf
    expensive_item = None 

    for _, items in inventory.items():
        for _, item in items.items():
            price = item.get("price", 0)
            if price > max_price:
                max_price = price
                expensive_item = item
    
    return expensive_item


def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for _, items in inventory.items():
        for prod, item in items.items():
            if prod == item_name:
                if item.get("quantity", 0) > 0:
                    return item
                else:
                    return None

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    all_data = []

    for _, items in inventory.items():
        for _, item in items.items():
            all_data.append(item)

    return all_data

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    cat_it_pairs = []

    for cat1, items in inventory.items():
        for cat2, _ in items.items():
            cat_it_pairs.append((cat1, cat2))
    return cat_it_pairs

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    return deepcopy(inventory) if deep else inventory.copy()