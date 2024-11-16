class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []

    def push(self, data):
        # Add an element to the top of the stack
        self.stack.append(data)

    def pop(self):
        # Remove and return the top element from the stack
        # If the stack is not empty, pop the last element; otherwise, return an error message
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"  # Handle empty stack scenario

    def peek(self):
        # Return the top element without removing it from the stack
        # If the stack is not empty, return the last element; otherwise, return an error message
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"  # Handle empty stack scenario

    def is_empty(self):
        # Check if the stack is empty by comparing its length to 0
        return len(self.stack) == 0

# Test the Stack class
stack = Stack()  # Create a new stack instance
stack.push(10)  # Push 10 onto the stack
stack.push(20)  # Push 20 onto the stack
stack.push(30)  # Push 30 onto the stack

# Peek to see the top element of the stack
print("Top element:", stack.peek())  # Output: 30

# Pop the top element from the stack
print("Popped element:", stack.pop())  # Output: 30

# Print the stack after popping an element
print("Stack after pop:", stack.stack)  # Output: [10, 20]
