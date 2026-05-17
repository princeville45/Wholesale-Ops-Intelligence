import math

def economic_order_quantity(annual_demand, ordering_cost, holding_cost_per_unit):
    """Calculates the EOQ to minimize total inventory costs."""
    if holding_cost_per_unit == 0: return float('inf')
    return round(math.sqrt((2 * annual_demand * ordering_cost) / holding_cost_per_unit), 2)