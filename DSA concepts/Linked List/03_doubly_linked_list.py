"""
DOUBLY LINKED LIST
==================

A doubly linked list is similar to a singly linked list, but each node
has TWO pointers:
- next: points to the next node
- prev: points to the previous node

This allows traversal in BOTH directions (forward and backward).

Example: None ← [10|↕] ↔ [20|↕] ↔ [30|↕] → None
                  |      |      |
                 prev   data  next
"""


class Node:
    """
    Node for doubly linked list.
    
    Attributes:
        data: The value stored in this node
        next: Reference to the next node
        prev: Reference to the previous node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    A doubly linked list implementation.
    """
    
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
    
    def append(self, data):
        """
        Add element at the end of the list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        # Find the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Add new node
        current.next = new_node
        new_node.prev = current
    
    def prepend(self, data):
        """
        Add element at the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        # Insert at the beginning
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def display_forward(self):
        """Print list from head to tail (forward direction)."""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("→ ".join(elements) + " →")
    
    def display_backward(self):
        """
        Print list from tail to head (backward direction).
        This is a key advantage of doubly linked lists!
        """
        if self.head is None:
            print("← ")
            return
        
        # Find the last node first
        current = self.head
        while current.next:
            current = current.next
        
        # Traverse backward
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        print("← ".join(elements) + " ←")
    
    def insert_after(self, target_data, new_data):
        """
        Insert a new node after a node with specific data.
        
        Example: If list is [10, 20, 30]
                 insert_after(20, 25) results in [10, 20, 25, 30]
        
        Time Complexity: O(n)
        """
        new_node = Node(new_data)
        current = self.head
        
        # Find the node with target_data
        while current and current.data != target_data:
            current = current.next
        
        if current is None:
            print(f"Node with data {target_data} not found!")
            return
        
        # Insert new node after current
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        
        current.next = new_node
    
    def delete(self, data):
        """
        Delete the first node with specific data.
        Time Complexity: O(n)
        """
        current = self.head
        
        # Find the node to delete
        while current and current.data != data:
            current = current.next
        
        if current is None:
            print(f"Node with data {data} not found!")
            return
        
        # Handle deletion
        if current.prev:
            current.prev.next = current.next
        else:
            # Deleting the head node
            self.head = current.next
        
        if current.next:
            current.next.prev = current.prev
    
    def get_length(self):
        """Get the number of nodes in the list."""
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DOUBLY LINKED LIST - FORWARD AND BACKWARD TRAVERSAL")
    print("=" * 70)
    
    # Create and populate the doubly linked list
    dll = DoublyLinkedList()
    for val in [10, 20, 30, 40, 50]:
        dll.append(val)
    
    # 1. Display forward
    print("\n1. FORWARD TRAVERSAL (using next pointers):")
    print("   ", end="")
    dll.display_forward()
    
    # 2. Display backward (unique to doubly linked lists!)
    print("\n2. BACKWARD TRAVERSAL (using prev pointers):")
    print("   This is UNIQUE to doubly linked lists!")
    print("   ", end="")
    dll.display_backward()
    
    # 3. Insert at beginning
    print("\n3. INSERT AT BEGINNING (5):")
    dll.prepend(5)
    print("   Forward:  ", end="")
    dll.display_forward()
    
    # 4. Insert after a specific node
    print("\n4. INSERT AFTER NODE WITH DATA 30 (new data: 35):")
    dll.insert_after(30, 35)
    print("   Forward:  ", end="")
    dll.display_forward()
    print("   Backward: ", end="")
    dll.display_backward()
    
    # 5. Delete a node
    print("\n5. DELETE NODE WITH DATA 20:")
    dll.delete(20)
    print("   Forward:  ", end="")
    dll.display_forward()
    print("   Backward: ", end="")
    dll.display_backward()
    
    # 6. Get length
    print(f"\n6. LENGTH OF THE LIST: {dll.get_length()}")
    
    print("\n" + "=" * 70)
