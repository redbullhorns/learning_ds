class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node with the given data to the end of the list."""
        temp_Node = Node(data)
        if self.head is None:
            self.head = temp_Node
            return self.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = temp_Node
            return self.head

    def prepend(self, data):
        """Add a node with the given data to the beginning of the list."""
        if self.head is None:
            self.head = Node(data)
            return self.head
        else:
            temp_Node = Node(data)
            temp_Node.next = self.head
            self.head = temp_Node
            return self.head

    def delete_with_value(self, data):
        """Delete the first node with the given data."""
        if self.head.data == data:
            self.head = self.head.next
            return self.head
        else:
            current = self.head
            previous = None
            while current:
                if current.data == data:
                    previous.next = current.next
                    return self.head
                previous = current
                current = current.next
                
    def find(self, data):
        """Find a node with the given data."""
        if self.head is None:
            return None
        if self.head.data == data:
            return self.head
        current = self.head
        while current.next:
            if current.data == data:
                return current
            current = current.next

    def print_list(self):
        """Print all the nodes in the list."""
        current = self.head
        while current:
            print(current.data)
            current = current.next