import pandas as pd
import numpy as np

np.random.seed(42)

# Define Menu Items with Current Prices and Ingredient/Production Costs
menu_data = [
    {"item_id": "ITM_01", "item_name": "Whopper Meal", "category": "Meals", "current_price": 12.50, "unit_cost": 4.80},
    {"item_id": "ITM_02", "item_name": "Double Whopper Meal", "category": "Meals", "current_price": 15.50, "unit_cost": 6.20},
    {"item_id": "ITM_03", "item_name": "Cheeseburger", "category": "Burgers", "current_price": 4.50, "unit_cost": 1.70},
    {"item_id": "ITM_04", "item_name": "Bacon Cheese Burger", "category": "Burgers", "current_price": 6.80, "unit_cost": 2.60},
    {"item_id": "ITM_05", "item_name": "Large Fries", "category": "Sides", "current_price": 4.20, "unit_cost": 0.90},
    {"item_id": "ITM_06", "item_name": "Medium Onion Rings", "category": "Sides", "current_price": 4.50, "unit_cost": 1.10},
    {"item_id": "ITM_07", "item_name": "Large Soft Drink", "category": "Drinks", "current_price": 3.80, "unit_cost": 0.45},
    {"item_id": "ITM_08", "item_name": "Bottled Water", "category": "Drinks", "current_price": 3.50, "unit_cost": 0.60},
    {"item_id": "ITM_09", "item_name": "Sundae Ice Cream", "category": "Desserts", "current_price": 4.00, "unit_cost": 1.20},
    {"item_id": "ITM_10", "item_name": "Apple Pie", "category": "Desserts", "current_price": 3.00, "unit_cost": 0.95}
]

df_menu = pd.DataFrame(menu_data)

# Simulate 1 Year of Transaction Volume per Item
# Popular items get high volume, specialty items get moderate volume
annual_volumes = [45000, 22000, 68000, 31000, 85000, 41000, 95000, 18000, 29000, 24000]
df_menu['annual_units_sold'] = annual_volumes

# Calculate Core Financial Metrics
df_menu['gross_revenue'] = df_menu['current_price'] * df_menu['annual_units_sold']
df_menu['total_cogs'] = df_menu['unit_cost'] * df_menu['annual_units_sold']
df_menu['total_gross_profit'] = df_menu['gross_revenue'] - df_menu['total_cogs']
df_menu['contribution_margin_per_unit'] = df_menu['current_price'] - df_menu['unit_cost']
df_menu['food_cost_pct'] = round((df_menu['unit_cost'] / df_menu['current_price']) * 100, 2)

# Menu Engineering Classification (Boston Consulting Group Matrix Model)
# High Profit / High Popularity = STAR
# Low Profit / High Popularity = PLOWHORSE
# High Profit / Low Popularity = PUZZLE
# Low Profit / Low Popularity = DOG
avg_profit = df_menu['total_gross_profit'].mean()
avg_volume = df_menu['annual_units_sold'].mean()

def classify_item(row):
    if row['total_gross_profit'] >= avg_profit and row['annual_units_sold'] >= avg_volume:
        return 'Star (High Profit, High Volume)'
    elif row['total_gross_profit'] < avg_profit and row['annual_units_sold'] >= avg_volume:
        return 'Plowhorse (Low Profit, High Volume)'
    elif row['total_gross_profit'] >= avg_profit and row['annual_units_sold'] < avg_volume:
        return 'Puzzle (High Profit, Low Volume)'
    else:
        return 'Dog (Low Profit, Low Volume)'

df_menu['menu_classification'] = df_menu.apply(classify_item, axis=1)

# Propose Next Year Pricing (Simulating a 4% Inflation Adjustment + Margin Optimization)
def suggest_new_price(row):
    if 'Star' in row['menu_classification'] or 'Puzzle' in row['menu_classification']:
        # We can safely raise price slightly on high-profit or premium items
        return round(row['current_price'] * 1.05, 2)
    elif 'Plowhorse' in row['menu_classification']:
        # High volume item, small bump or repackage recipe to lower cost
        return round(row['current_price'] * 1.03, 2)
    else:
        # Dog items - consider deprecating or keeping flat
        return row['current_price']

df_menu['recommended_next_year_price'] = df_menu.apply(suggest_new_price, axis=1)
df_menu['projected_next_year_revenue'] = df_menu['recommended_next_year_price'] * df_menu['annual_units_sold']
df_menu['projected_profit_gain'] = df_menu['projected_next_year_revenue'] - df_menu['gross_revenue']

# Export dataset for Tableau
df_menu.to_csv("menu_profitability_analysis.csv", index=False)
print("Dataset 'menu_profitability_analysis.csv' generated successfully!")