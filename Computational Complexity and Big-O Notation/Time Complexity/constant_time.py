# Function to get the first element of an array
def get_first_element(arr):
    # The function accesses the first element of the list (array) by index 0.
    # This operation always takes constant time, O(1), regardless of the size of the array.
    return arr[0]

# Test case
arr = [10, 20, 30, 40, 50]
# The expected output is the first element of the array, which is 10.
print("First element:", get_first_element(arr))  # Output: 10
