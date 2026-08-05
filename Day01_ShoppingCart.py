#SHOPPING CART

cart = {}
while True:
    name_Pro = input("Enter item name (or 'done' to finish):")
    if name_Pro.lower() == "done":
        break
    price_Pro = float(input(f'Enter price for {name_Pro}:'))
    cart[name_Pro] = price_Pro

total = sum(cart.values())
print(cart)
print(f'The total cost of items purchased is: ${total}')

