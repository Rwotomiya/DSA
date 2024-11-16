def merge_sort(arr):
    if len(arr) > 1:  # Only proceed if the array has more than 1 element
        mid = len(arr) // 2  # Find the middle index of the array
        left_half = arr[:mid]  # Split the array into the left half
        right_half = arr[mid:]  # Split the array into the right half

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize indices for left_half, right_half, and arr
        # Merge the sorted left and right halves
        while i < len(left_half) and j < len(right_half):  # Compare elements in both halves
            if left_half[i] < right_half[j]:  # If element in left_half is smaller
                arr[k] = left_half[i]  # Place it in the correct position of the original array
                i += 1  # Move to the next element in left_half
            else:  # If element in right_half is smaller
                arr[k] = right_half[j]  # Place it in the correct position of the original array
                j += 1  # Move to the next element in right_half
            k += 1  # Move to the next position in the original array

        # If there are remaining elements in left_half, add them to arr
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # If there are remaining elements in right_half, add them to arr
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Return the sorted array

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", merge_sort(arr))
