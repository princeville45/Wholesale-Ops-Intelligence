"""
Inventory Demand Forecasting Engine
Author: Irem Victor Chinonso | Statistical Business Architect
Date: 2026-05-12
Repo: Wholesale-Ops-Intelligence

Forecasts next-week demand for SKUs at a wholesale depot
using exponential smoothing and trend decomposition.
Flags potential stockouts and overstock situations.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


SKUS = ["20L Pure Water", "10L Pure Water", "5L Pure Water", "Sachet Box", "Mini Bottle 50cl"]


def generate_weekly_sales(skus, weeks=12):
    """Simulate 12 weeks of weekly sales per SKU."""
    np.random.seed(99)
    records = []
    base = {"20L Pure Water": 180, "10L Pure Water": 120, "5L Pure Water": 90,
            "Sachet Box": 250, "Mini Bottle 50cl": 60}

    for week in range(1, weeks + 1):
        for sku in skus:
            b = base[sku]
            seasonal = np.sin(week / 12 * 2 * np.pi) * b * 0.15
            noise = np.random.normal(0, b * 0.08)
            qty = max(0, int(b + seasonal + noise))
            records.append({"week": week, "sku": sku, "qty_sold": qty})

    return pd.DataFrame(records)


def exponential_smoothing(series, alpha=0.3):
    """Apply simple exponential smoothing to a series."""
    smoothed = [series.iloc[0]]
    for val in series.iloc[1:]:
        smoothed.append(alpha * val + (1 - alpha) * smoothed[-1])
    return smoothed


def forecast_next_week(df, alpha=0.3):
    """Forecast demand for each SKU using exponential smoothing."""
    results = []
    for sku in df["sku"].unique():
        series = df[df["sku"] == sku].sort_values("week")["qty_sold"]
        smoothed = exponential_smoothing(series, alpha)
        forecast = round(alpha * series.iloc[-1] + (1 - alpha) * smoothed[-1])
        avg_weekly = round(series.mean(), 1)
        max_weekly = series.max()
        min_weekly = series.min()
        results.append({
            "sku": sku,
            "last_week_actual": series.iloc[-1],
            "forecast_next_week": forecast,
            "avg_weekly_sales": avg_weekly,
            "peak_week": max_weekly,
            "trough_week": min_weekly
        })
    return pd.DataFrame(results)


def flag_stock_risks(forecast_df, current_stock):
    """Compare forecast to current stock and flag risks."""
    forecast_df = forecast_df.copy()
    forecast_df["current_stock"] = forecast_df["sku"].map(current_stock)
    forecast_df["stock_gap"] = forecast_df["current_stock"] - forecast_df["forecast_next_week"]

    def risk(row):
        if row["stock_gap"] < 0:
            return "STOCKOUT RISK"
        elif row["stock_gap"] > row["forecast_next_week"] * 1.5:
            return "OVERSTOCK"
        else:
            return "ADEQUATE"

    forecast_df["risk_flag"] = forecast_df.apply(risk, axis=1)
    return forecast_df


def run_forecast():
    print("=" * 60)
    print("INVENTORY DEMAND FORECASTING ENGINE")
    print("Wholesale Ops Intelligence | Irem Victor Chinonso")
    print("=" * 60)

    df = generate_weekly_sales(SKUS, weeks=12)
    forecast_df = forecast_next_week(df)

    current_stock = {
        "20L Pure Water": 150,
        "10L Pure Water": 200,
        "5L Pure Water": 60,
        "Sachet Box": 300,
        "Mini Bottle 50cl": 40
    }

    risk_df = flag_stock_risks(forecast_df, current_stock)

    print("\n--- NEXT WEEK DEMAND FORECAST ---")
    print(risk_df[["sku", "last_week_actual", "forecast_next_week",
                    "current_stock", "stock_gap", "risk_flag"]].to_string(index=False))

    print("\n--- ACTION ITEMS ---")
    for _, row in risk_df.iterrows():
        if row["risk_flag"] == "STOCKOUT RISK":
            reorder = abs(int(row["stock_gap"])) + int(row["forecast_next_week"] * 0.2)
            print(f"  REORDER ALERT: {row['sku']} — order at least {reorder} units")
        elif row["risk_flag"] == "OVERSTOCK":
            print(f"  SLOW-MOVE: {row['sku']} — consider promotions or reduced reorder")

    print("\nForecast complete.")


if __name__ == "__main__":
    run_forecast()
