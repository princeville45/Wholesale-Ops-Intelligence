def inventory_turnover_ratio(cogs, avg_inventory):
    """Calculates the inventory turnover ratio for performance benchmarking."""
    if avg_inventory == 0: return 0
    return round(cogs / avg_inventory, 2)