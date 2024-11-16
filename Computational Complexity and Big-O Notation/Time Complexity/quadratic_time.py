# Function to print all pairs of elements from the array
def print_pairs(arr):
    # Outer loop iterates through each element of the array
    for i in range(len(arr)):
        # Inner loop iterates through each element of the array again
        for j in range(len(arr)):
            print(arr[i], arr[j])  # Print the pair of elements (arr[i], arr[j])

# Test case
arr = [1, 2, 3]
# Expected output is all combinations of pairs: (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)
print_pairs(arr)
