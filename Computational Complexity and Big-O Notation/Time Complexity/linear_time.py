# Function to print all elements of an array
def print_all_elements(arr):
    # Loop through each element in the array
    # The loop will run once for each element, so it takes O(n) time, where n is the number of elements in the array.
    for element in arr:
        print(element)  # Print the current element

# Test case
arr = [10, 20, 30, 40, 50]
# The expected output is the list of elements in the array, one per line.
print_all_elements(arr)
