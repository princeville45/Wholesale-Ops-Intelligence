def identify_stockout_risk(inventory_df):
    """Flags SKUs where sales velocity exceeds remaining stock lead time."""
    inventory_df['days_left'] = inventory_df['stock_on_hand'] / inventory_df['avg_daily_sales']
    risky_skus = inventory_df[inventory_df['days_left'] <= inventory_df['lead_time_days']]
    return risky_skus[['sku', 'days_left', 'lead_time_days']]