def calculate_reorder_point(avg_daily_sales, lead_time_days, safety_stock):
    """Calculates the Reorder Point (ROP) for a specific SKU."""
    rop = (avg_daily_sales * lead_time_days) + safety_stock
    return round(rop, 2)