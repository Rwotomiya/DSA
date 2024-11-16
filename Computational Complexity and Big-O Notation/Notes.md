# Analyzing the Complexity of Sorting and Searching Algorithms

## Sorting Algorithms

### 1. Bubble Sort
- **Time Complexity:** O(n^2) – Due to the nested loops where each element is compared with every other element.
- **Space Complexity:** O(1) – Bubble Sort is an in-place sorting algorithm, meaning it doesn’t require extra space beyond the input array.

### 2. Merge Sort
- **Time Complexity:** O(n log n) – Merge Sort divides the array into halves (log n divisions) and merges them (n operations for each division).
- **Space Complexity:** O(n) – Merge Sort requires additional space to store temporary arrays for merging.

### 3. Quick Sort
- **Time Complexity:** O(n log n) (on average) – Quick Sort partitions the array based on a pivot, dividing the array into subarrays and sorting them recursively. Worst case (O(n^2)) occurs when the pivot is always the smallest or largest element.
- **Space Complexity:** O(log n) – Quick Sort is an in-place algorithm, so it doesn't require much extra space for recursion.

### 4. Insertion Sort
- **Time Complexity:** O(n^2) – Due to the nested loop, which shifts elements to make room for the current element.
- **Space Complexity:** O(1) – It sorts in-place.

## Searching Algorithms

### 1. Linear Search
- **Time Complexity:** O(n) – We check each element of the array one by one.
- **Space Complexity:** O(1) – No extra space is required.

### 2. Binary Search (on a sorted array)
- **Time Complexity:** O(log n) – Each step halves the size of the remaining search space.
- **Space Complexity:** O(1) – Binary search does not require extra space besides the input array.

## How to Evaluate Time and Space Complexity

1. **Identify the Operations:** Look for loops, recursion, or repetitive tasks that determine the number of operations the algorithm will perform as input grows.

2. **Count the Operations:** Examine how many times the algorithm performs significant operations, like iterating through an array or calling a recursive function.

3. **Express the Growth:** Relate the number of operations to the input size (n). For nested loops, you might end up with a squared term (O(n^2)), or for recursion, you could have a logarithmic or exponential term (O(log n) or O(2^n)).

4. **Simplify the Big-O Notation:** Focus on the most significant term and remove constants. For example, O(3n + 2) simplifies to O(n), and O(n^2 + n) simplifies to O(n^2).
