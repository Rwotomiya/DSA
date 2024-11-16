# Simple hash function based on the length of the key
# This function takes a string 'key' as input and returns the length of the string.
# The idea is to use the length of the string as a simple hash value.
def simple_hash(key):
    return len(key)  # Simple hash function: return the length of the string as the hash value

# Test
key = "Alice"
# Testing the hash function with the key 'Alice'.
# The expected output is the length of the string "Alice", which is 5.
print("Hash for 'Alice':", simple_hash(key))  # Output: 5 (length of 'Alice')
