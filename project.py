
item_descriptions = [
    "Food Accessories",
    "Home Accessories",
    "Books",
    "Electric Parts",
    "Cloth"
] 
item_prices = [100, 200, 350, 500, 250] 
item_quantities = [650, 300, 350, 100, 70]
total_purchase = 0

print("Item Prices:")
print("1. Food Accessories = 100 Taka per piece.")
print("2. Home Accessories = 200 Taka per piece.")
print("3. Books = 350 Taka per piece.")
print("4. Electric Parts = 500 Taka per piece.")
print("5. Cloth = 250 Taka per piece.")

print("\nTo start shopping, first create your account.")
name = input("Enter your Name: ")
email = input("Enter your email address: ")
password = input("Enter a password: ")
print("Account created successfully!")

is_logged_in = False

while not is_logged_in:
    entered_email = input("Please enter your email address: ")
    entered_password = input("Please enter your password: ")

    if entered_email == email and entered_password == password:
        is_logged_in = True
        print(f"Welcome, {name}!")
    else:
        print("Invalid email or password. Please try again.")

is_done_shopping = False

while not is_done_shopping:
    print("\nPlease select an item to purchase:")
    for i in range(5):
        print(f"{i+1}. {item_descriptions[i]} - {item_prices[i]} Taka (quantity: {item_quantities[i]})")

    selected_item = int(input()) - 1

    if selected_item < 0 or selected_item >= 5:
        print("Invalid selection.")
        continue

    quantity = int(input(f"Please enter the quantity of item {selected_item + 1} you would like to purchase: "))

    if quantity > item_quantities[selected_item]:
        print(f"We have limited quantity for Item {selected_item + 1}.")
        continue

    item_quantities[selected_item] -= quantity
    total_price = item_prices[selected_item] * quantity

    print(f"You have selected {quantity} of item {selected_item + 1}.")
    print(f"The total price is {total_price} Taka.")

    total_purchase += total_price

    if total_purchase > 20000:
        discount = total_purchase * 0.1
        discounted_total = total_purchase - discount
        print("Congratulations! You qualify for a 10% discount.")
        print(f"Your total purchase amount is {total_purchase} Taka, and after discount your total amount is {discounted_total} Taka.")
    else:
        print(f"Your total purchase is {total_purchase} Taka.")

    print("\nPlease select a payment method:")
    print("1. BKash")
    print("2. Nagad")
    print("3. Banking")

    payment_method = int(input())

    if payment_method == 1:
        print("Please make payment to bKash account 01234567890.")
    elif payment_method == 2:
        print("Please make payment to Nagad account 01234567890.")
    elif payment_method == 3:
        print("Please make payment to our bank account No - 012345678911011.")
    else:
        print("Invalid selection.")
        continue

    response = input("Would you like to make another purchase? (y/n): ")

    if response.lower() == 'n':
        is_done_shopping = True


print("Thank you for shopping with us!")
