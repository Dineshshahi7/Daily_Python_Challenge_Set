'''
# Problem : You are given a list of customer orders. Your task is to analyze the data and generate key business insights using Python.

Dataset (given as list of dictionaries)
orders = [
    {"customer": "Aarav", "product": "Tea", "quantity": 3, "price": 50},
    {"customer": "Sita", "product": "Coffee", "quantity": 2, "price": 80},
    {"customer": "Aarav", "product": "Coffee", "quantity": 1, "price": 80},
    {"customer": "Ravi", "product": "Tea", "quantity": 5, "price": 50},
    {"customer": "Sita", "product": "Tea", "quantity": 4, "price": 50},
]
Task 1
Create a new field:
total_spent = quantity * price

Task 2
Find:
Total spending per customer

Task 3
Find:
Most valuable customer (highest spending)

Task 4
Find:
Total revenue per product

Task 5
Print simple insights:

Who spends the most?
Which product gives highest revenue?
'''

orders = [
    {"customer": "Aarav", "product": "Tea", "quantity": 3, "price": 50},
    {"customer": "Sita", "product": "Coffee", "quantity": 2, "price": 80},
    {"customer": "Aarav", "product": "Coffee", "quantity": 1, "price": 80},
    {"customer": "Ravi", "product": "Tea", "quantity": 5, "price": 50},
    {"customer": "Sita", "product": "Tea", "quantity": 4, "price": 50},
]

# 🔹 Step 1: Add total_spent
for order in orders:
    order["total_spent"] = order["quantity"] * order["price"]

# 🔹 Step 2: Customer-wise total spending
customer_spending = {}

for order in orders:
    customer = order["customer"]
    customer_spending[customer] = customer_spending.get(customer, 0) + order["total_spent"]

print("Customer Spending:", customer_spending)

# 🔹 Step 3: Most valuable customer
top_customer = max(customer_spending, key=customer_spending.get)
print("Top Customer:", top_customer)

# 🔹 Step 4: Product-wise revenue
product_revenue = {}

for order in orders:
    product = order["product"]
    product_revenue[product] = product_revenue.get(product, 0) + order["total_spent"]

print("Product Revenue:", product_revenue)

# 🔹 Step 5: Insights
top_product = max(product_revenue, key=product_revenue.get)

print("\nINSIGHTS:")
print(f"1. Top customer is {top_customer} with highest spending.")
print(f"2. Highest revenue product is {top_product}.")