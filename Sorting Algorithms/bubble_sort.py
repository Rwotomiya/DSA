def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    # Outer loop for n iterations (n elements in the array)
    for i in range(n):
        # Inner loop to perform the comparisons and swap elements
        # After each pass, the largest element will be at the end of the array
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  # If the current element is greater than the next
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
    return arr  # Return the sorted array

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))
