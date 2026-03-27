'''
# E-commerce Cart System (Functions + OOP Optional)

- Simulate a shopping cart system.

i) Requirements:
- Predefined product list:
    { "laptop": 80000, "phone": 30000, "tablet": 20000 }

ii) Features:
- Add product to cart
- Remove product
- View cart
- Calculate total price

iii) Logic:
- Allow multiple quantities
- Show bill with:
- item name
- quantity
- total price

iv) Bonus:
- Apply discount:
- If total > 100000 → 10% discount
'''

# predefine product list
products = {
    "laptop": 80000,
    "phone": 30000,
    "tablet": 20000
}

# shopping cart dictionary
cart = {}

# function to add products to cart 
def add_to_cart():
    print("\nAvailable products:", ", ".join(products.keys()))
    item = input("Enter product name to add: ").lower()
    if item in products:
        qty = int(input(f"Enter quantity of {item}: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"{qty} {item}(s) added to cart.")
    else:
        print("Product not found.")

# Function to remove product from cart
def remove_from_cart():
    if not cart:
        print("Cart is empty.")
        return
    item = input("Enter product name to remove: ").lower()
    if item in cart:
        qty = int(input(f"Enter quantity of {item} to remove: "))
        if qty >= cart[item]:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            cart[item] -= qty
            print(f"{qty} {item}(s) removed from cart.")
    else:
        print("Item not in cart.")

# Function to view cart and bill
def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    print("{:<10} {:<10} {:<10}".format("Item", "Quantity", "Price"))
    for item, qty in cart.items():
        price = products[item] * qty
        total += price
        print("{:<10} {:<10} {:<10}".format(item, qty, price))
    
    # Apply discount if total > 100000
    discount = 0
    if total > 100000:
        discount = total * 0.1
        total -= discount
        print(f"\nDiscount applied: {discount}")
    
    print(f"\nTotal Price: {total}")

# Main loop
def main():
    while True:
        print("\n1. Add to Cart")
        print("2. Remove from Cart")
        print("3. View Cart")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_to_cart()
        elif choice == "2":
            remove_from_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main()