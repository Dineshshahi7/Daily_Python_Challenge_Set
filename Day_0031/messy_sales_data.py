'''
Problem: Messy Sales Data
You are given a messy dataset:
data = [
    "A, 10, $5.5",
    "B, 5, $3",
    "A, 7, $5.5",
    "C, , $4",        
    "B, 3, $3",
    "A, 2, $5.5",
    "C, 4, $4"
]

✅ 1. Clean the data
Remove $ from price
Convert quantity & price to numbers
Ignore rows where quantity is missing

✅ 2. Calculate total sales per product
👉 Formula: Total = quantity × price

Output:
{
    "A": 104.5,
    "B": 24,
    "C": 16
}

✅ 3. Find the product with highest sales
Output:
"A"
✅ 4. Bonus (Important 🔥)
Sort products by total sales (highest → lowest)
'''

data = [
    "A, 10, $5.5",
    "B, 5, $3",
    "A, 7, $5.5",
    "C, , $4",
    "B, 3, $3",
    "A, 2, $5.5",
    "C, 4, $4"
]

sales = {}

for row in data:
    parts = row.split(",")
    
    name = parts[0].strip()
    qty = parts[1].strip()
    price = parts[2].strip().replace("$", "")
    
    if qty == "":
        continue
    
    qty = int(qty)
    price = float(price)
    
    total = qty * price
    
    if name not in sales:
        sales[name] = 0
    
    sales[name] += total

# Highest sales product
top_product = max(sales, key=sales.get)

# Sorted result
sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)

print("Sales:", sales)
print("Top Product:", top_product)
print("Sorted:", sorted_sales)