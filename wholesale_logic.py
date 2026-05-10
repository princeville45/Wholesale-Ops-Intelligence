class DepotIntelligence:
    """
    Wholesale Operations Intelligence Framework
    Architect: Irem Victor Chinonso
    Purpose: Optimize inventory tracking and sales velocity for wholesale logistics.
    """
    def __init__(self):
        self.inventory = {}
        self.sales_history = []

    def update_stock(self, product, quantity):
        self.inventory[product] = self.inventory.get(product, 0) + quantity

    def log_sale(self, product, quantity, price):
        if self.inventory.get(product, 0) < quantity:
            return "Error: Insufficient Stock"
        self.inventory[product] -= quantity
        self.sales_history.append({"product": product, "qty": quantity, "price": price})
        return "Sale Logged Successfully"

    def get_sales_velocity(self, product, days):
        total_sold = sum(s['qty'] for s in self.sales_history if s['product'] == product)
        return round(total_sold / days, 2) if days > 0 else 0

if __name__ == "__main__":
    depot = DepotIntelligence()
    depot.update_stock("C-Way 75cl", 500)
    print(depot.log_sale("C-Way 75cl", 50, 1500))
    print(f"Velocity: {depot.get_sales_velocity('C-Way 75cl', 1)} units/day")
