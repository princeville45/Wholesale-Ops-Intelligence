import math
def calculate_safety_stock(avg_demand, lead_time, service_level=1.65):
    std_dev = avg_demand * 0.2
    return math.ceil(service_level * std_dev * math.sqrt(lead_time))