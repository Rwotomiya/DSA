class Node:
    def __init__(self, data):
        self.data = data  # Stores the data of the node
        self.next = None  # Points to the next node in the list, initially set to None

class LinkedList:
    def __init__(self):
        self.head = None  # The head of the list is initially None, indicating an empty list

    def append(self, data):
        # Create a new node with the provided data
        new_node = Node(data)

        # If the list is empty (i.e., head is None), set the new node as the head
        if not self.head:
            self.head = new_node
            return

        # Otherwise, traverse the list to find the last node
        last = self.head
        while last.next:  # Loop until the last node (which has no 'next')
            last = last.next  # Move to the next node
        
        # Set the next pointer of the last node to the new node
        last.next = new_node

    def print_list(self):
        # Start from the head of the list
        temp = self.head

        # Traverse the list and print the data of each node
        while temp:
            print(temp.data, end=" -> ")  # Print the current node's data followed by an arrow
            temp = temp.next  # Move to the next node
        
        # After the list traversal, print "None" to indicate the end of the list
        print("None")

# Test the LinkedList implementation
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append a node with data 1 to the list
ll.append(2)  # Append a node with data 2 to the list
ll.append(3)  # Append a node with data 3 to the list

# Print the entire linked list
ll.print_list()  # Expected Output: 1 -> 2 -> 3 -> None
