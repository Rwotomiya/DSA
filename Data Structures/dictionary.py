# Creating a hash map (dictionary)
# A dictionary in Python is a data structure that stores key-value pairs.
# It allows fast lookups, insertions, and deletions based on the key.
hash_map = {}

# Insert key-value pairs into the hash map
# The key is the unique identifier, and the value is the associated data.
# For example, the key "name" is associated with the value "Alice".
hash_map["name"] = "Alice"  # Add a key-value pair: 'name' -> 'Alice'
hash_map["age"] = 30        # Add a key-value pair: 'age' -> 30
hash_map["city"] = "Gulu"   # Add a key-value pair: 'city' -> 'Gulu'

# Search for a value by key
# The value associated with a specific key can be accessed using the key.
# In this case, we're retrieving the value associated with the key 'name'.
print("Name:", hash_map["name"])  # Output: Alice

# Delete a key-value pair from the hash map
# The 'del' statement removes a key-value pair by specifying the key.
# Here, we're removing the key 'age' and its associated value.
del hash_map["age"]

# Print the updated hash map
# After deletion, the hash map will no longer contain the key 'age'.
print("Updated hash map:", hash_map)  # Output: {'name': 'Alice', 'city': 'Gulu'}
