# Computational Complexity

Computational Complexity is a way to describe the efficiency of an algorithm, particularly in terms of time and space usage as the input size grows. Big-O notation is used to express this efficiency.

## Big-O Notation

Big-O notation provides an upper bound for an algorithm's growth rate, which means it describes the worst-case scenario. It helps us understand how the algorithm will perform as the input size grows.

## Common Big-O Complexities

### O(1) – Constant Time
The execution time or space required is independent of the size of the input. For example, accessing an element in an array by index is O(1).

### O(log n) – Logarithmic Time
The execution time grows logarithmically with the input size. Binary search is an example of an O(log n) algorithm.

### O(n) – Linear Time
The execution time grows linearly with the size of the input. A simple loop through an array to find an element is O(n).

### O(n log n) – Linearithmic Time
Algorithms with time complexity between linear and quadratic, such as Merge Sort or Quick Sort, typically have O(n log n) time complexity.

### O(n^2) – Quadratic Time
The execution time grows quadratically with the input size. Common in algorithms with nested loops, like Bubble Sort or Selection Sort.

### O(2^n) – Exponential Time
The execution time doubles with each additional element in the input. Algorithms that solve problems like the Traveling Salesman Problem or Fibonacci recursion without memoization are exponential.

### O(n!) – Factorial Time
The execution time grows extremely fast with the input size. Algorithms that generate permutations or solve problems like N-Queens can have factorial time complexity.
