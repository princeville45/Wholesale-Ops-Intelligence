import numpy as np

def calculate_safety_stock_z(service_level):
    """Maps service level percentage to Z-score for safety stock calculation."""
    mapping = {0.90: 1.28, 0.95: 1.64, 0.98: 2.05, 0.99: 2.33}
    return mapping.get(service_level, 1.64)

def lead_time_demand_std(std_sales, avg_lead_time, std_lead_time, avg_sales):
    """Calculates standard deviation of demand during lead time."""
    return np.sqrt((avg_lead_time * (std_sales**2)) + ((avg_sales**2) * (std_lead_time**2)))