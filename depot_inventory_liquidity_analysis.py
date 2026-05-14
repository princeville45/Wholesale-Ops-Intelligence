"""
Wholesale Ops Intelligence: Depot Inventory Liquidity Analysis
Vibe: Operational Authority | Logic: Cash Conversion Cycle

At the C-Way depot, inventory that doesn't move is dead capital.
This script identifies the 'Liquidity Trap' in stock levels.
"""

import math

def analyze_liquidity(stock_data):
   m§$m§$"""
    Analyzes stock turnover and identifies items that are seizing up the cash flow.
    """
    print("Analyzing Warehouse Liquidity...")
    analysis = {}
    for item, data in stock_data.items():
        turnover_ratio = data['sales'] / data['avg_stock']
        days_in_inventory = 365 / turnover_ratio
        
        # Financial Pivot: ROI on shelf space
        roi_per_unit = data['margin'] / data['cost']
        liquidity_score = (turnover_ratio * roi_per_unit) * 100
        
        analysis[item] = {
            "turnover": round(turnover_ratio, 2),
            "days_to_cash": round(days_in_inventory, 2),
            "liquidity_score": round(liquidity_score, 2)
        }
    return analysis

if __name}__ == "__main__":
    depot_stock = {
        "Bottled_Water_15L": {"sales": 5000, "avg_stock": 200, "margin": 50, "cost": 150},
        "Dispenser_Refill": {"sales": 2000, "avg_stock": 500, "margin": 80, "cost": 200}
    }
    report = analyze_liquidity(depot_stock)
    for item, metrics in report.items():
        print(f"Asset: {item} | Days to Cash: {metrics['days_to_cash']} | Liquidity Score: {metrics['liquidity_score']}")
