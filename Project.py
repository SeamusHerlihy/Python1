# Inventory Management System

inventory = []

# Add an item to the inventory
def add_item():
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ").strip()

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"Item '{name}' added successfully.\n")

# Update an item in the inventory
def update_item():
    name = input("Enter the name of the item to update: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            item["price"] = float(input("Enter new price: "))
            item["quantity"] = int(input("Enter new quantity: "))
            item["category"] = input("Enter new category: ").strip()

            print(f"Item '{name}' updated successfully.\n")
            return

    print("Item not found.\n")

# View the inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return

    print("\n--- Inventory List ---")
    for item in inventory:
        print(f"Name: {item['name']}")
        print(f"Price: ${item['price']:.2f}")
        print(f"Quantity: {item['quantity']}")
        print(f"Category: {item['category']}")
        print("----------------------")
    print()

# Remove an item from the inventory
def remove_item():
    name = input("Enter the name of the item to remove: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"Item '{name}' removed successfully.\n")
            return

    print("Item not found.\n")

# Search the inventory by category
def search_by_category():
    category = input("Enter category to search: ").strip().lower()
    found = False

    print(f"\nItems in category '{category}':")
    for item in inventory:
        if item["category"].lower() == category:
            print(f"- {item['name']} (${item['price']:.2f}, Qty: {item['quantity']})")
            found = True

    if not found:
        print("No items found under this category.")
    print()

# Main function
def main():
    while True:
        print("=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Closing program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()
