# Initialize the inventory dictionary
inventory = {
    "apple": {"quantity": 50, "price": 0.5},
    "banana": {"quantity": 100, "price": 0.2},
    "orange": {"quantity": 75, "price": 0.3}
}

# Function to add a new item to the inventory
def add_item(name, quantity, price):
    if name in inventory:
        print(f"Item '{name}' already exists in the inventory.")
    else:
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"Item '{name}' added to the inventory.")

# Function to update the quantity and price of an existing item
def update_item(name, quantity, price):
    if name in inventory:
        inventory[name]["quantity"] = quantity
        inventory[name]["price"] = price
        print(f"Item '{name}' updated in the inventory.")
    else:
        print(f"Item '{name}' does not exist in the inventory.")

# Function to remove an item from the inventory
def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed from the inventory.")
    else:
        print(f"Item '{name}' does not exist in the inventory.")

# Function to retrieve information about a specific item
def get_item_info(name):
    if name in inventory:
        return inventory[name]
    else:
        return f"Item '{name}' does not exist in the inventory."

# Function to list all items in the inventory
def list_inventory():
    for name, info in inventory.items():
        print(f"Item: {name}, Quantity: {info['quantity']}, Price: ${info['price']}")

# Example usage
print("Initial inventory:")
list_inventory()

print("\nAdding a new item:")
add_item("grape", 200, 0.4)
list_inventory()

print("\nUpdating an existing item:")
update_item("banana", 120, 0.25)
list_inventory()

print("\nRemoving an item:")
remove_item("orange")
list_inventory()

print("\nRetrieving information about an item:")
item_info = get_item_info("apple")
print(f"Apple info: {item_info}")

print("\nFinal inventory:")
list_inventory()