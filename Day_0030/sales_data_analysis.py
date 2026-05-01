'''
Sales Data Analysis System

You are given a dataset like this:

data = [
    {"product": "Rice", "category": "Food", "qty": 50, "price": 120},
    {"product": "Flour", "category": "Food", "qty": 30, "price": 80},
    {"product": "Oil", "category": "Food", "qty": 20, "price": 150},
    {"product": "Soap", "category": "Non-Food", "qty": 40, "price": 60},
    {"product": "Shampoo", "category": "Non-Food", "qty": 25, "price": 200},
    {"product": "Rice", "category": "Food", "qty": 70, "price": 115},
]
🎯 Your Tasks
✅ 1. Add a new key:
👉 total = qty * price

✅ 2. Find:
Total revenue of all products
Revenue per category

✅ 3. Find:
👉 Top selling product (by total revenue)

✅ 4. Group data:
👉 Combine same products (Rice appears twice)

Expected:
Rice → total qty, avg price, total revenue
✅ 5. Find anomaly:
👉 Any product where price differs more than 20% from its average price
'''

data = [
    {"product": "Rice", "category": "Food", "qty": 50, "price": 120},
    {"product": "Flour", "category": "Food", "qty": 30, "price": 80},
    {"product": "Oil", "category": "Food", "qty": 20, "price": 150},
    {"product": "Soap", "category": "Non-Food", "qty": 40, "price": 60},
    {"product": "Shampoo", "category": "Non-Food", "qty": 25, "price": 200},
    {"product": "Rice", "category": "Food", "qty": 70, "price": 115},
]

# 1. Add total
for item in data:
    item["total"] = item["qty"] * item["price"]

# 2. Total revenue
total_revenue = sum(item["total"] for item in data)
print("Total Revenue:", total_revenue)

# Revenue per category
category_revenue = {}
for item in data:
    cat = item["category"]
    category_revenue[cat] = category_revenue.get(cat, 0) + item["total"]

print("Revenue per category:", category_revenue)

# 3. Top selling product
top_product = max(data, key=lambda x: x["total"])
print("Top Product:", top_product["product"])

# 4. Group products
grouped = {}

for item in data:
    name = item["product"]
    if name not in grouped:
        grouped[name] = {"qty": 0, "total": 0, "prices": []}
    
    grouped[name]["qty"] += item["qty"]
    grouped[name]["total"] += item["total"]
    grouped[name]["prices"].append(item["price"])

# Calculate avg price
for name, val in grouped.items():
    avg_price = sum(val["prices"]) / len(val["prices"])
    print(f"{name}: Qty={val['qty']}, Avg Price={avg_price:.2f}, Revenue={val['total']}")

# 5. Detect anomaly
print("\nAnomalies:")
for name, val in grouped.items():
    avg_price = sum(val["prices"]) / len(val["prices"])
    
    for price in val["prices"]:
        if abs(price - avg_price) / avg_price > 0.2:
            print(f"{name} has unusual price: {price}")