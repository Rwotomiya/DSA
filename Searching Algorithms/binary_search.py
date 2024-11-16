def binary_search(arr, target):
    low = 0  # Set the low index to 0, which is the start of the array
    high = len(arr) - 1  # Set the high index to the last element in the array
    while low <= high:  # Continue as long as the low index is less than or equal to the high index
        mid = (low + high) // 2  # Find the middle index of the current sub-array
        if arr[mid] == target:  # If the middle element is equal to the target, return the index
            return mid
        elif arr[mid] < target:  # If the middle element is less than the target, discard the left half
            low = mid + 1  # Move the low index to mid + 1
        else:  # If the middle element is greater than the target, discard the right half
            high = mid - 1  # Move the high index to mid - 1
    return -1  # Return -1 if the target is not found in the array

# Test
arr = [2, 3, 4, 10, 40]  # Sorted array
target = 10  # Element to search for
result = binary_search(arr, target)  # Perform binary search on the array
print(f"Element found at index {result}" if result != -1 else "Element not found")
