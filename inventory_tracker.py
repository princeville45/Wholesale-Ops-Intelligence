"""
Wholesale Ops Intelligence — Inventory Tracker
Real-time stock level monitoring with restock alerts.
Built for C-Way Depot, Ife, Nigeria.
"""

import json
from datetime import datetime


RESTOCK_THRESHOLD = 50  # units


def load_inventory(filepath="inventory.json"):
    """Load current inventory from JSON file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_inventory(inventory, filepath="inventory.json"):
    """Persist updated inventory."""
    with open(filepath, "w") as f:
        json.dump(inventory, f, indent=2)


def log_movement(product, quantity, movement_type, filepath="movement_log.json"):
    """Log every stock movement with timestamp."""
    try:
        with open(filepath, "r") as f:
            log = json.load(f)
    except FileNotFoundError:
        log = []

    log.append({
        "timestamp": datetime.now().isoformat(),
        "product": product,
        "quantity": quantity,
        "type": movement_type  # "sale" or "restock"
    })

    with open(filepath, "w") as f:
        json.dump(log, f, indent=2)


def record_sale(product, quantity):
    """Deduct sold units and check restock threshold."""
    inventory = load_inventory()

    if product not in inventory:
        print(f"[ERROR] Product '{product}' not found in inventory.")
        return

    current_stock = inventory[product]["stock"]

    if quantity > current_stock:
        print(f"[WARNING] Insufficient stock for '{product}'. Available: {current_stock}")
        return

    inventory[product]["stock"] -= quantity
    inventory[product]["last_updated"] = datetime.now().isoformat()
    save_inventory(inventory)
    log_movement(product, quantity, "sale")

    new_stock = inventory[product]["stock"]
    print(f"[SALE] {product}: -{quantity} units. Remaining: {new_stock}")

    if new_stock <= RESTOCK_THRESHOLD:
        print(f"[ALERT] RESTOCK REQUIRED: '{product}' is low ({new_stock} units remaining)")


def record_restock(product, quantity):
    """Add restocked units to inventory."""
    inventory = load_inventory()

    if product not in inventory:
        inventory[product] = {"stock": 0, "last_updated": None}

    inventory[product]["stock"] += quantity
    inventory[product]["last_updated"] = datetime.now().isoformat()
    save_inventory(inventory)
    log_movement(product, quantity, "restock")

    print(f"[RESTOCK] {product}: +{quantity} units. Total: {inventory[product]['stock']}")


def get_stock_report():
    """Print full inventory status."""
    inventory = load_inventory()
    print("\n--- INVENTORY REPORT ---")
    print(f"{'Product':<30} {'Stock':>8} {'Status':<15}")
    print("-" * 55)
    for product, data in inventory.items():
        stock = data["stock"]
        status = "LOW - RESTOCK" if stock <= RESTOCK_THRESHOLD else "OK"
        print(f"{product:<30} {stock:>8} {status:<15}")
    print("-" * 55)


if __name__ == "__main__":
    # Demo run
    get_stock_report()
