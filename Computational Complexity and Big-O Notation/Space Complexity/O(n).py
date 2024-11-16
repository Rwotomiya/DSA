# Function to create a copy of the given array
def create_copy(arr):
    copy = arr[:]  # Creates a shallow copy of the array using slicing. The space needed grows with the size of the input array.
    return copy  # Returns the newly created copy of the array

# Test case
arr = [1, 2, 3, 4, 5]
# The expected output is a new array that is a copy of the original one: [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Copy of the array:", create_copy(arr))  # Output: [1, 2, 3, 4, 5]
