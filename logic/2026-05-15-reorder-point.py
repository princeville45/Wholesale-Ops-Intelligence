import math

def calculate_rop(avg_daily_demand, lead_time_days, safety_stock):
    """Calculates the Reorder Point (ROP) for a warehouse SKU."""
    return (avg_daily_demand * lead_time_days) + safety_stock