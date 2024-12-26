import random  # Used for generating random numbers and selecting random recommendations.
import time  # Provides functions for time delays, such as controlling the typewriter effect.
import sys # Enables interaction with system-specific functions, like flushing the output buffer for the typewriter effect.
import msvcrt  # Import for checking key presses (Windows-only) so that we can use space bar to skip the type writing animation.

# This the Function for typewriter effect with the skip option.
def typewriter(text, delay=0.02):
    """Displays text with a typewriter effect, and allows the user to skip."""
    idx = 0
    while idx < len(text):
        if msvcrt.kbhit():  # This part Check if a key is pressed.
            if msvcrt.getch() == b' ':  # Space bar is pressed.
                sys.stdout.write(text[idx:])  # Then Print the remaining text.
                sys.stdout.flush()
                break
        sys.stdout.write(text[idx])
        sys.stdout.flush()
        idx += 1
        time.sleep(delay)
    print()

# Function to show random recommendations at the start.
def display_recommendations():
    recommendations = [
        "Pair a Latte with a Classic Roll for the perfect afternoon treat!",
        "Enjoy a Frappuccino with Pecan Rolls for a refreshing and nutty delight.",
        "A Hot Matcha Latte goes great with a Caramel Roll.",
        "Try Iced Coffee and 4 Rolls Bundle for a group snack!",
        "Start your day with a Green Tea and a Classic Roll."
    ]
    typewriter("\n--- 🌟 **Today's Recommendations** 🌟 ---")
    typewriter(f"🛒 {random.choice(recommendations)}")  # This line of code with the import random Shows a random recommendation.

# Displaying the menu.
def display_menu():
    typewriter("\n--- 🍵 **Menu** ☕ ---")
    typewriter("\n--- ☕ **Hot & Cold Coffees** 🍪 ---")
    typewriter("  1. ☕ Hot Coffee (Espresso, Latte, Cappuccino)")
    typewriter("  2. 🧊 Cold Coffee (Iced Coffee, Frappuccino)")
    typewriter("\n--- 🍃 **Tea & Matcha Delights** 🌱 ---")
    typewriter("  3. 🍵 Tea (Green Tea, Black Tea, Chai)")
    typewriter("  4. 🍃 Matcha (Hot & Iced Matcha Latte)")  
    typewriter("\n--- 🍩 **Sweet Snacks** 🍪 ---")
    typewriter("  5. 🍩 Cinnamon Rolls (Classic, Pecan, Caramel)")
    typewriter("  6. 🍯 Snack Bundles (2 Rolls, 4 Rolls, 6 Rolls)")

# Function to calculate total price with any additions(syrup, sugar, etc.).
def calculate_price(base_price, syrup_price=0, sugar_price=0):
    return base_price + syrup_price + sugar_price

# Function to handle payment methods.
def payment_method(total_price, purchases):
    typewriter("\n💵 **Select Payment Method:**")
    typewriter("  1. Cash 💵")
    typewriter("  2. Card 💳")

    while True:
        payment_choice = input("\nChoose your payment method (1 or 2): ").strip()

        if payment_choice == "1":  # The Cash Payment prompt.
            while True:
                try:
                    cash_inserted = float(input(f"\nPlease insert ${total_price:.2f} or more: $"))
                    if cash_inserted < total_price:
                        typewriter(f"❌ You have inserted ${cash_inserted:.2f}, but need ${total_price:.2f}. Please insert more.")
                    else:
                        change = cash_inserted - total_price
                        typewriter(f"💸 Payment successful! Your change is ${change:.2f}.")
                        print_item_dispensing()
                        print_receipt(purchases, total_price)
                        return
                except ValueError:
                    typewriter("❌ Invalid amount. Please enter a valid number.")
        elif payment_choice == "2":  # The Card Payment prompt.
            while True:
                try:
                    card_balance = float(input("\nEnter your card balance: $"))
                    if card_balance < total_price:
                        typewriter(f"❌ Insufficient funds. You need ${total_price - card_balance:.2f} more.")
                    else:
                        card_balance -= total_price
                        typewriter(f"\n💳 Payment successful! Your remaining card balance is ${card_balance:.2f}.")
                        print_item_dispensing()
                        print_receipt(purchases, total_price)
                        return
                except ValueError:
                    typewriter("❌ Invalid amount. Please enter a valid number.")
        else:
            typewriter("❌ Invalid option. Please choose 1 for cash or 2 for card.")

# Function to print a receipt.
def print_receipt(purchases, total_price):
    typewriter("\n--- 🧾 **Receipt** ---")
    for item in purchases:
        typewriter(f"- {item[0]}: ${item[1]:.2f}")
    typewriter(f"\nTotal: ${total_price:.2f}")
    typewriter("--- Thank you for shopping with us! ---\n")

# Dispensing animation that also has the 3 second delay.
def print_item_dispensing():
    typewriter("\n🔄 **Item is being dispensed...**", delay=0.2)
    for _ in range(3):
        typewriter(".", delay=0.5)
    typewriter("✅ **Item has now been dispensed!**\n")

# Function to check if an item is in stock.
def check_stock(item, stock):
    if stock[item] > 0:
        return True
    else:
        typewriter(f"❌ Sorry, {item} is out of stock.")
        return False

# Function to update the stock after a purchase.
def update_stock(item, stock):
    stock[item] -= 1
    typewriter(f"📦 {item} stock has been updated. Remaining stock: {stock[item]}")

# Additional recommendations before payment.
def display_additional_recommendations():
    options = [
        ("Latte", 3.50),
        ("Classic Roll", 2.00),
        ("Frappuccino", 4.00)
    ]
    typewriter("\n--- 🍴 **Would You Like to Add This?** 🍴 ---")
    recommendation = random.choice(options)
    typewriter(f"🛍️ Would you like to add a {recommendation[0]} for ${recommendation[1]:.2f}?")

    # Ask the user if they want to add the item or continue to payment.
    user_choice = input("\nEnter '1' to add this item or '2' to not add: ").strip()

    if user_choice == "1":
        print_item_added_to_order(recommendation)  # Show confirmation.
        return recommendation  # Return the item and price as a tuple.
    elif user_choice == "2":
        typewriter("❌ Item not added. Proceeding to the next step.")  # Notification for not adding item.
     
# Confirmation that the item has been added to the order.
def print_item_added_to_order(item):
    typewriter(f"\n✅ **{item[0]} has been added to your order for ${item[1]:.2f}.**")

# Main vending machine logic.
def vending_machine():
    stock = {
        "Espresso": 5, "Latte": 5, "Cappuccino": 5,
        "Iced Coffee": 5, "Frappuccino": 5,
        "Green Tea": 5, "Black Tea": 5, "Chai": 5,
        "Hot Matcha Latte": 5, "Iced Matcha Latte": 5,
        "Classic Roll": 5, "Pecan Roll": 5, "Caramel Roll": 5,
        "2 Rolls": 5, "4 Rolls": 5, "6 Rolls": 5
    }

    menu = {
        "Coffee": {
            "Hot": [{"name": "Espresso", "price": 2.00}, {"name": "Latte", "price": 3.50}, {"name": "Cappuccino", "price": 3.00}],
            "Cold": [{"name": "Iced Coffee", "price": 2.50}, {"name": "Frappuccino", "price": 4.00}]
        },
        "Tea": [{"name": "Green Tea", "price": 2.00}, {"name": "Black Tea", "price": 2.00}, {"name": "Chai", "price": 2.50}],
        "Matcha": [{"name": "Hot Matcha Latte", "price": 4.00}, {"name": "Iced Matcha Latte", "price": 4.50}],
        "Snacks": {
            "Cinnamon Rolls": [{"name": "Classic Roll", "price": 2.00}, {"name": "Pecan Roll", "price": 2.50}, {"name": "Caramel Roll", "price": 2.50}],
            "Bundles": {"2 Rolls": 4.00, "4 Rolls": 7.50, "6 Rolls": 10.00}
        }
    }

    total_price = 0
    purchases = []

    typewriter("\n🍵 **Welcome to The Coffee House!** ☕")
    display_recommendations()

    while True:
        display_menu()
        user_choice = input("\nSelect an option (1, 2, 3, 4, 5, 6): ").strip()

        # Coffee (Hot or Cold).
        if user_choice == "1" or user_choice == "2":  
            coffee_type = "Hot" if user_choice == "1" else "Cold"
            typewriter(f"\nAvailable options for {coffee_type} Coffee:")
            for i, coffee in enumerate(menu["Coffee"][coffee_type]):
                typewriter(f"  {i + 1}. {coffee['name']} - ${coffee['price']:.2f}")
            coffee_choice = int(input(f"Select your {coffee_type} coffee (1, 2, etc.): ")) - 1
            coffee_name = menu["Coffee"][coffee_type][coffee_choice]["name"]

            if not check_stock(coffee_name, stock):
                continue

            base_price = menu["Coffee"][coffee_type][coffee_choice]["price"]

            typewriter("\nWould you like Caramel syrup for $0.50?")
            syrup_choice = input("Enter '1' for Yes, '2' for No: ").strip()
            syrup_price = 0.5 if syrup_choice == '1' else 0
            if syrup_price:
                typewriter(f"🧃 You added Caramel syrup for an extra $0.50.")

            typewriter("\nHow many sugar packs would you like? Each pack costs $0.10.")
            sugar_packs = int(input("Enter number of sugar packs: "))
            sugar_price = sugar_packs * 0.10
            if sugar_price:
                typewriter(f"🍬 You added {sugar_packs} sugar pack(s) for an extra ${sugar_price:.2f}.")
                
            drink_price = calculate_price(base_price, syrup_price, sugar_price)
            total_price += drink_price
            purchases.append((coffee_name, drink_price))

            update_stock(coffee_name, stock)
            typewriter(f"\nYou selected {coffee_name} with syrup and {sugar_packs} sugar(s). Total cost: ${drink_price:.2f}")   

        # Tea.
        elif user_choice == "3":
            typewriter("\nAvailable options for Tea:")
            for i, tea in enumerate(menu["Tea"]):
                typewriter(f"  {i + 1}. {tea['name']} - ${tea['price']:.2f}")
            tea_choice = int(input(f"Select your tea (1, 2, etc.): ")) - 1
            tea_name = menu["Tea"][tea_choice]["name"]

            if not check_stock(tea_name, stock):
                continue

            base_price = menu["Tea"][tea_choice]["price"]
            total_price += base_price
            purchases.append((tea_name, base_price))

            update_stock(tea_name, stock)
            typewriter(f"\nYou selected {tea_name}. Total cost: ${base_price:.2f}")

        # Matcha.
        elif user_choice == "4":
            typewriter("\nAvailable options for Matcha:")
            for i, matcha in enumerate(menu["Matcha"]):
                typewriter(f"  {i + 1}. {matcha['name']} - ${matcha['price']:.2f}")
            matcha_choice = int(input(f"Select your matcha (1, 2, etc.): ")) - 1
            matcha_name = menu["Matcha"][matcha_choice]["name"]

            if not check_stock(matcha_name, stock):
                continue

            base_price = menu["Matcha"][matcha_choice]["price"]
            total_price += base_price
            purchases.append((matcha_name, base_price))

            update_stock(matcha_name, stock)
            typewriter(f"\nYou selected {matcha_name}. Total cost: ${base_price:.2f}")

        # Cinnamon Rolls.
        elif user_choice == "5":
            typewriter("\nAvailable options for Cinnamon Rolls:")
            for i, roll in enumerate(menu["Snacks"]["Cinnamon Rolls"]):
                typewriter(f"  {i + 1}. {roll['name']} - ${roll['price']:.2f}")
            roll_choice = int(input(f"Select your roll (1, 2, etc.): ")) - 1
            roll_name = menu["Snacks"]["Cinnamon Rolls"][roll_choice]["name"]

            if not check_stock(roll_name, stock):
                continue

            base_price = menu["Snacks"]["Cinnamon Rolls"][roll_choice]["price"]
            total_price += base_price
            purchases.append((roll_name, base_price))

            update_stock(roll_name, stock)
            typewriter(f"\nYou selected {roll_name}. Total cost: ${base_price:.2f}")

        # Snack Bundles.
        elif user_choice == "6":
            typewriter("\nAvailable Snack Bundles:")
            bundles = list(menu["Snacks"]["Bundles"].items())
            for i, (bundle, price) in enumerate(bundles, 1):
                typewriter(f"  {i}. {bundle} - ${price:.2f}")

            bundle_choice = input("Enter your bundle choice (1, 2, or 3): ").strip()

            if bundle_choice in ["1", "2", "3"]:
                bundle_index = int(bundle_choice) - 1 
                bundle_name, bundle_price = bundles[bundle_index]
                total_price += bundle_price
                purchases.append((bundle_name, bundle_price))

                update_stock(bundle_name, stock)
                typewriter(f"\nYou selected {bundle_name}. Total cost: ${total_price:.2f}")
            else:
                typewriter("❌ Invalid bundle choice.")

        # After item selection, this prompts user to continue shopping, add item, or go to payment.
        recommendation = display_additional_recommendations()

        if recommendation:
            if recommendation == "continue":
                continue
            purchases.append((recommendation[0], recommendation[1]))  # This Add's the recommended item to the purchases list.
            total_price += recommendation[1]  # It now Add the cost to the total price.

        # Prompt below ask user if they want to pay or continue shopping.
        typewriter("\nWould you like to proceed to payment or continue shopping?")
        user_choice = input("\nEnter '1' to pay, '2' to continue shopping: ").strip()

        if user_choice == "1": 
            typewriter("\n💳 Proceeding to payment...")
            payment_method(total_price, purchases)
            break
        elif user_choice == "2":
            typewriter("\n🛒 Continuing shopping...")
            continue
        else:
            typewriter("❌ Invalid option. Returning to payment process.")
            payment_method(total_price, purchases)
            break

vending_machine() # This line of code is here so It runs

# Play the Code to Start!
# After starting just press from 1-6 depending on the instructions provided just press the numbers that is fit to your needs. 
# Enjoy The Coffee House Vending Machine!!! 