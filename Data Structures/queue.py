class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def enqueue(self, data):
        # Add an element to the rear (end) of the queue
        self.queue.append(data)

    def dequeue(self):
        # Remove and return the element from the front of the queue
        # If the queue is not empty, pop the first element; otherwise, return an error message
        if not self.is_empty():
            return self.queue.pop(0)  # pop(0) removes the first element (FIFO behavior)
        else:
            return "Queue is empty!"  # Handle empty queue scenario

    def front(self):
        # Return the front element of the queue without removing it
        # If the queue is not empty, return the first element; otherwise, return an error message
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty!"  # Handle empty queue scenario

    def is_empty(self):
        # Check if the queue is empty by comparing its length to 0
        return len(self.queue) == 0

# Test the Queue class
queue = Queue()  # Create a new queue instance
queue.enqueue(10)  # Add 10 to the queue
queue.enqueue(20)  # Add 20 to the queue
queue.enqueue(30)  # Add 30 to the queue

# Peek to see the front element of the queue
print("Front element:", queue.front())  # Output: 10

# Dequeue the front element from the queue
print("Dequeued element:", queue.dequeue())  # Output: 10

# Print the queue after dequeuing an element
print("Queue after dequeue:", queue.queue)  # Output: [20, 30]
