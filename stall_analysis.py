# ==========================================
# Gikomba Market Stall Performance Analysis
# ==========================================

# Dataset provided for the assignment
daily_sales = [2300, 1950, 2800, 2100, 3600, 5200, 4100,
               2500, 2200, 3100, 2400, 3900, 5600, 4700]   # 14 days, KES
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] * 2

# qty = kg in stock, reorder = reorder level (kg), cost/price = KES per kg
stock = {
    "Tomatoes": {"qty": 18, "reorder": 25, "cost": 60, "price": 90},
    "Onions":   {"qty": 40, "reorder": 20, "cost": 70, "price": 100},
    "Sukuma":   {"qty": 9,  "reorder": 15, "cost": 30, "price": 50},
    "Potatoes": {"qty": 55, "reorder": 30, "cost": 50, "price": 75},
    "Avocado":  {"qty": 12, "reorder": 10, "cost": 80, "price": 140},
}

print("=== 1. TOTALS AND EXTREMES ===")
total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)
max_sale = max(daily_sales)
min_sale = min(daily_sales)

best_index = daily_sales.index(max_sale)
worst_index = daily_sales.index(min_sale)

best_day_name = days[best_index]
worst_day_name = days[worst_index]
best_week = 1 if best_index <= 6 else 2
worst_week = 1 if worst_index <= 6 else 2

print(f"Total 14-Day Sales: KES {total_sales:,}")
print(f"Average Daily Sales: KES {average_sales:,.2f}")
print(f"Highest Sale: KES {max_sale:,} on {best_day_name} (Week {best_week})")
print(f"Lowest Sale: KES {min_sale:,} on {worst_day_name} (Week {worst_week})\n")


print("=== 2. WEEK-ON-WEEK GROWTH ===")
def week_totals(sales):
    """Return a tuple of (week 1 total, week 2 total) using slicing."""
    week1 = sum(sales[0:7])
    week2 = sum(sales[7:14])
    return week1, week2

w1_total, w2_total = week_totals(daily_sales)
wow_growth = ((w2_total - w1_total) / w1_total) * 100
print(f"Week 1 Total: KES {w1_total:,}")
print(f"Week 2 Total: KES {w2_total:,}")
print(f"Week-on-Week Growth: {wow_growth:.2f}%\n")


print("=== 3. DAY CLASSIFICATION ===")
def classify_day(amount, average):
    """Return 'Strong', 'Normal', or 'Weak' based on 20% threshold from average."""
    if amount > average * 1.2:
        return "Strong"
    elif amount < average * 0.8:
        return "Weak"
    else:
        return "Normal"

day_counts = {}
for sale in daily_sales:
    status = classify_day(sale, average_sales)
    day_counts[status] = day_counts.get(status, 0) + 1

for status, count in day_counts.items():
    print(f"{status} days: {count}")
print()


print("=== 4. WEEKDAYS VS WEEKENDS ===")
weekdays_sales = daily_sales[0:5] + daily_sales[7:12]   # Mon-Fri for both weeks
weekends_sales = daily_sales[5:7] + daily_sales[12:14]  # Sat-Sun for both weeks

avg_weekday = sum(weekdays_sales) / len(weekdays_sales)
avg_weekend = sum(weekends_sales) / len(weekends_sales)
diff_pct = ((avg_weekend - avg_weekday) / avg_weekday) * 100

print(f"Average Weekday Sales: KES {avg_weekday:,.2f}")
print(f"Average Weekend Sales: KES {avg_weekend:,.2f}")
print(f"Weekend vs Weekday Difference: {diff_pct:.2f}%\n")


print("=== 5. INVENTORY & GROSS MARGIN ===")
def check_reorder(stock_dict):
    """Return a list of products whose quantity is at or below reorder level."""
    reorder_list = []
    for item, info in stock_dict.items():
        if info["qty"] <= info["reorder"]:
            reorder_list.append(item)
    return reorder_list

items_to_restock = check_reorder(stock)
print(f"Products to Restock: {items_to_restock}")
print("Gross Margins:")
for item, info in stock.items():
    margin = (info["price"] - info["cost"]) / info["price"] * 100
    print(f"- {item}: {margin:.1f}%")
print()


print("=== 6. STALL PERFORMANCE REPORT ===")
print("--------------------------------------------------")
print("          WANJIKU'S STALL PERFORMANCE REPORT      ")
print("--------------------------------------------------")
print(f"Total Sales (14 Days)  : KES {total_sales:,.2f}")
print(f"Average Daily Sales    : KES {average_sales:,.2f}")
print(f"Week 1 Total           : KES {w1_total:,.2f}")
print(f"Week 2 Total           : KES {w2_total:,.2f}")
print(f"Week-on-Week Growth    : {wow_growth:.2f}%")
print(f"Weekend Premium        : +{diff_pct:.2f}% vs Weekdays")
print(f"Items Needing Restock  : {', '.join(items_to_restock)}")
print("--------------------------------------------------")