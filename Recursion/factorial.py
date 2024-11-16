def factorial(n):
    # Base case: If n is 0, return 1 because the factorial of 0 is defined as 1
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        # This calls the function itself with a smaller value, reducing the problem size
        return n * factorial(n - 1)

# Test the factorial function
print(factorial(5))  # Output: 120
