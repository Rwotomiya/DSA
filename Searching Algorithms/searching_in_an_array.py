# Function to search for an element in the array
def searchEle(arr, n, key):
    """
    This function performs a linear search to find the position
    of the 'key' in the array 'arr'.
    
    Parameters:
    arr: list - The array to search in.
    n: int - The size of the array.
    key: int - The element to search for.
    
    Returns:
    int - The index of the element if found; otherwise, -1.
    """
    # Loop through the array
    for i in range(n):
        # Check if the current element matches the key
        if arr[i] == key:
            return i  # Return the index if found
    return -1  # Return -1 if the key is not found


# Driver code
if __name__ == '__main__':
    # Initialize the array and key
    arr = [24, 53, 64, 2, 54, 35, 4, 25]  # The array of elements
    key = 25  # The element to search for
    n = len(arr)  # Get the length of the array

    # Call the search function
    index = searchEle(arr, n, key)

    # Output the result
    if index != -1:
        # Element found: Output the 1-based position
        print("Element found at position: " + str(index + 1))
    else:
        # Element not found
        print("Element not found")
