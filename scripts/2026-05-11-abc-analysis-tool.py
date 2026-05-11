import pandas as pd

def perform_abc_analysis(products_data):
    """
    Performs ABC analysis on inventory data.
    products_data: list of dicts with 'name', 'units_sold', 'unit_price'
    """
    df = pd.DataFrame(products_data)
    df['revenue'] = df['units_sold'] * df['unit_price']
    df = df.sort_values(by='revenue', ascending=False)
    
    df['cum_revenue'] = df['revenue'].cumsum()
    total_revenue = df['revenue'].sum()
    df['cum_perc'] = (df['cum_revenue'] / total_revenue) * 100
    
    def classify(perc):
        if perc <= 80: return 'A'
        if perc <= 95: return 'B'
        return 'C'
    
    df['class'] = df['cum_perc'].apply(classify)
    return df

if __name__ == "__main__":
    inventory = [
        {"name": "C-Way 75cl Box", "units_sold": 500, "unit_price": 1200},
        {"name": "C-Way 1.5L Box", "units_sold": 300, "unit_price": 1500},
        {"name": "C-Way Dispenser Jar", "units_sold": 100, "unit_price": 800},
        {"name": "Small Cup Water", "units_sold": 1000, "unit_price": 50},
        {"name": "Premium Sparkling", "units_sold": 50, "unit_price": 2500},
    ]
    
    results = perform_abc_analysis(inventory)
    print("--- ABC Inventory Classification ---")
    print(results[['name', 'revenue', 'cum_perc', 'class']])
