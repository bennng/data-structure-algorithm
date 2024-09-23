# Initialize a set of guests
guest_list = {"Alice", "Bob", "Charlie"}

# Print the initial guest list
print("Initial guest list:", guest_list)

# Add a new guest
guest_list.add("David")
print("Guest list after adding David:", guest_list)

# Try to add a duplicate guest
guest_list.add("Alice")
print("Guest list after trying to add Alice again:", guest_list)

# Remove a guest
guest_list.remove("Charlie")
print("Guest list after removing Charlie:", guest_list)

# Check if a guest is on the list
print("Is Bob on the guest list?", "Bob" in guest_list)
print("Is Charlie on the guest list?", "Charlie" in guest_list)

# List all guests
print("Final guest list:")
for guest in guest_list:
    print(guest)