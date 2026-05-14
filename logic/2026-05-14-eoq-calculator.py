import math

def calculate_eoq(annual_demand, order_cost, holding_cost_per_unit):
    """Calculates the Economic Order Quantity (EOQ)."""
    if holding_cost_per_unit == 0: return 0
    eoq = math.sqrt((2 * annual_demand * order_cost) / holding_cost_per_unit)
    return round(eoq)