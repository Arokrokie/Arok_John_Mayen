# Inventory Management System

stock_items = {
    "Laptop": {"quantity": 10, "price": 899.99},
    "Smartphone": {"quantity": 25, "price": 499.99},
    "Monitor": {"quantity": 15, "price": 199.99},
    "Keyboard": {"quantity": 30, "price": 49.99},
    "Mouse": {"quantity": 40, "price": 24.99},
}

inventory = stock_items.copy()

while True:
    print("\n=== Inventory Management System ===")
    print("1. Add New Item")
    print("2. View Inventory")
    print("3. Update Item Quantity")
    print("4. Remove Item")
    print("5. Restock Default Items")
    print("6. Exit")

    action = (
        input("What would you like to do? (Enter action name or number): ")
        .strip()
        .lower()
    )

    # Add New Item
    if action in ["1", "add", "add new item"]:
        print("\nAvailable default items (not in inventory):")
        available_items = [item for item in stock_items if item not in inventory]

        if available_items:
            for i, item in enumerate(available_items, 1):
                print(f"{i}. {item}")
            print(f"{len(available_items)+1}. Add completely new item")

            item_selection = input(
                "Select item to add (enter number) or type new item name: "
            )

            try:
                # If user selects a number
                item_selection = int(item_selection)
                if 1 <= item_selection <= len(available_items):
                    item_name = available_items[item_selection - 1]
                    inventory[item_name] = stock_items[item_name].copy()
                    print(f"Added {item_name} to inventory with default values.")
                elif item_selection == len(available_items) + 1:
                    # Add completely new item
                    item_name = input("Enter new item name: ")
                    if item_name in inventory:
                        print("Item already exists in inventory.")
                    else:
                        while True:
                            try:
                                quantity = int(input("Enter quantity: "))
                                price = float(input("Enter price per unit: "))
                                inventory[item_name] = {
                                    "quantity": quantity,
                                    "price": price,
                                }
                                print(f"Item '{item_name}' added successfully!")
                                break
                            except ValueError:
                                print(
                                    "Please enter valid numbers for quantity and price."
                                )
                else:
                    print("Invalid selection.")
            except ValueError:
                # If user enters a new item name directly
                item_name = item_selection
                if item_name in inventory:
                    print("Item already exists in inventory.")
                else:
                    while True:
                        try:
                            quantity = int(input("Enter quantity: "))
                            price = float(input("Enter price per unit: "))
                            inventory[item_name] = {
                                "quantity": quantity,
                                "price": price,
                            }
                            print(f"Item '{item_name}' added successfully!")
                            break
                        except ValueError:
                            print("Please enter valid numbers for quantity and price.")
        else:
            item_name = input("Enter new item name: ")
            if item_name in inventory:
                print("Item already exists in inventory.")
            else:
                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        price = float(input("Enter price per unit: "))
                        inventory[item_name] = {"quantity": quantity, "price": price}
                        print(f"Item '{item_name}' added successfully!")
                        break
                    except ValueError:
                        print("Please enter valid numbers for quantity and price.")

    # View Inventory
    elif action in ["2", "view", "view inventory"]:
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            print(
                "{:<4} {:<20} {:<10} {:<10} {:<15}".format(
                    "No.", "Item", "Quantity", "Price", "Total Value"
                )
            )
            print("-" * 60)

            total_inventory_value = 0
            for i, (item, details) in enumerate(inventory.items(), 1):
                item_value = details["quantity"] * details["price"]
                total_inventory_value += item_value
                print(
                    "{:<4} {:<20} {:<10} ${:<9.2f} ${:<14.2f}".format(
                        i, item, details["quantity"], details["price"], item_value
                    )
                )

            print("-" * 60)
            print(f"{'Total Inventory Value:':<35} ${total_inventory_value:.2f}")

    # Update Item Quantity
    elif action in ["3", "update", "update quantity"]:
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nSelect item to update:")
            for i, item in enumerate(inventory.keys(), 1):
                print(f"{i}. {item}")

            try:
                item_num = int(input("Enter item number: "))
                if 1 <= item_num <= len(inventory):
                    item_name = list(inventory.keys())[item_num - 1]
                    while True:
                        try:
                            new_quantity = int(
                                input(
                                    f"Enter new quantity for {item_name} (current: {inventory[item_name]['quantity']}): "
                                )
                            )
                            inventory[item_name]["quantity"] = new_quantity
                            print(
                                f"Quantity for '{item_name}' updated to {new_quantity}."
                            )
                            break
                        except ValueError:
                            print("Please enter a valid number for quantity.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

    # Remove Item
    elif action in ["4", "remove", "remove item"]:
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nSelect item to remove:")
            for i, item in enumerate(inventory.keys(), 1):
                print(f"{i}. {item}")

            try:
                item_num = int(input("Enter item number: "))
                if 1 <= item_num <= len(inventory):
                    item_name = list(inventory.keys())[item_num - 1]
                    confirm = input(
                        f"Are you sure you want to remove {item_name}? (y/n): "
                    ).lower()
                    if confirm == "y":
                        del inventory[item_name]
                        print(f"Item '{item_name}' removed from inventory.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

    # Restock Default Items
    elif action in ["5", "restock", "restock defaults"]:
        confirm = input(
            "This will reset all default items to their original quantities. Continue? (y/n): "
        ).lower()
        if confirm == "y":
            for item in stock_items:
                if item in inventory:
                    inventory[item]["quantity"] = stock_items[item]["quantity"]
                else:
                    inventory[item] = stock_items[item].copy()
            print("Default items have been restocked.")

    # Exit Program
    elif action in ["6", "exit", "quit"]:
        print("Exiting Inventory Management System. Goodbye!")
        break

    # Invalid Action
    else:
        print("Invalid action. Please try again.")

    # Add a pause so user can see results before menu reappears
    input("\nPress Enter to continue...")
