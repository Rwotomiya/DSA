# Function to calculate the sum of all elements in an array
def sum_array(arr):
    total = 0  # Initialize a variable to keep track of the sum. This uses constant space (O(1)).
    
    # Loop through each number in the array
    for num in arr:
        total += num  # Add each element to the total sum
    
    return total  # Return the total sum of the array

# Test case
arr = [1, 2, 3, 4, 5]
# The expected output is the sum of the elements in the array: 1 + 2 + 3 + 4 + 5 = 15.
print("Sum of the array:", sum_array(arr))  # Output: 15
