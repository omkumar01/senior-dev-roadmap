"""
CIRCULAR LINKED LIST
====================

A circular linked list is a variation where the last node points back
to the first node instead of pointing to None.

This creates a CIRCLE - there's no real "end" to the list!

Visual representation:
    ┌─────────────────────────────┐
    │                             ↓
    [10 → 20 → 30 → 40 → 50] ──┘
    ↑                           (points back to 10)

Applications:
- Circular queues
- Round-robin scheduling
- Game loops where players take turns
"""


class Node:
    """Node for circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """
    A circular linked list implementation.
    """
    
    def __init__(self):
        """Initialize an empty circular linked list."""
        self.head = None
    
    def append(self, data):
        """
        Add element at the end of the list.
        The new node's next will point back to head (maintaining the circle).
        
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself (creates the circle)
            return
        
        # Find the last node
        current = self.head
        while current.next != self.head:  # Stop when we reach the node pointing to head
            current = current.next
        
        # Add new node and maintain the circle
        current.next = new_node
        new_node.next = self.head
    
    def prepend(self, data):
        """
        Add element at the beginning of the list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself
            return
        
        # Find the last node
        current = self.head
        while current.next != self.head:
            current = current.next
        
        # Insert new node at the beginning
        new_node.next = self.head
        current.next = new_node  # Last node now points to new node
        self.head = new_node
    
    def display(self):
        """
        Print the list. To avoid infinite loop, we print until we come
        back to the head node.
        """
        if self.head is None:
            print("Empty list")
            return
        
        elements = []
        current = self.head
        
        # Traverse until we reach head again
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        # Show it's circular by adding "..."
        print("" + " → ".join(elements) + " → (back to head) ⟲")
    
    def insert_after(self, target_data, new_data):
        """
        Insert a new node after a node with specific data.
        Time Complexity: O(n)
        """
        new_node = Node(new_data)
        current = self.head
        
        if self.head is None:
            print("List is empty!")
            return
        
        # Find the node with target_data
        while current.data != target_data:
            current = current.next
            if current == self.head:  # Completed the circle without finding target
                print(f"Node with data {target_data} not found!")
                return
        
        # Insert new node after current
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, data):
        """
        Delete the first node with specific data.
        Time Complexity: O(n)
        """
        if self.head is None:
            print("List is empty!")
            return
        
        # Special case: deleting the head
        if self.head.data == data:
            if self.head.next == self.head:  # Only one node
                self.head = None
                return
            
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Remove head
            current.next = self.head.next
            self.head = self.head.next
            return
        
        # Find the node to delete
        current = self.head
        prev = None
        
        while current.data != data:
            prev = current
            current = current.next
            if current == self.head:  # Completed the circle
                print(f"Node with data {data} not found!")
                return
        
        # Delete the node
        prev.next = current.next
    
    def get_length(self):
        """Get the number of nodes in the list."""
        if self.head is None:
            return 0
        
        count = 1
        current = self.head
        
        while current.next != self.head:
            count += 1
            current = current.next
        
        return count
    
    def traverse_n_steps(self, n_steps):
        """
        Traverse n steps starting from head and print the data.
        Useful for round-robin scheduling or simulations.
        
        Example: traverse_n_steps(7) in a list of 5 elements
                 will show: 10 → 20 → 30 → 40 → 50 → 10 → 20
        """
        if self.head is None:
            print("Empty list")
            return
        
        elements = []
        current = self.head
        
        for _ in range(n_steps):
            elements.append(str(current.data))
            current = current.next
        
        print("Traversing " + str(n_steps) + " steps: " + " → ".join(elements))


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("CIRCULAR LINKED LIST")
    print("=" * 70)
    
    # Create and populate circular linked list
    cll = CircularLinkedList()
    for val in [10, 20, 30, 40, 50]:
        cll.append(val)
    
    # 1. Display the circular list
    print("\n1. ORIGINAL CIRCULAR LIST:")
    print("   ", end="")
    cll.display()
    
    # 2. Add at the beginning
    print("\n2. PREPEND 5 AT THE BEGINNING:")
    cll.prepend(5)
    print("   ", end="")
    cll.display()
    
    # 3. Insert after specific node
    print("\n3. INSERT 25 AFTER NODE 20:")
    cll.insert_after(20, 25)
    print("   ", end="")
    cll.display()
    
    # 4. Get length
    print(f"\n4. LENGTH OF THE LIST: {cll.get_length()}")
    
    # 5. Traverse more steps than list length (demonstrates circularity)
    print("\n5. TRAVERSE 10 STEPS (more than list length of 6):")
    cll.traverse_n_steps(10)
    print("   Notice how it wraps around!")
    
    # 6. Delete a node
    print("\n6. DELETE NODE WITH DATA 20:")
    cll.delete(20)
    print("   ", end="")
    cll.display()
    
    # 7. Use case: Round-robin scheduling
    print("\n7. ROUND-ROBIN SCHEDULING (5 processes, 2 time units each):")
    cll2 = CircularLinkedList()
    processes = ['P1', 'P2', 'P3', 'P4', 'P5']
    for p in processes:
        cll2.append(p)
    
    print("   Executing processes with 2-unit time slices:")
    cll2.traverse_n_steps(10)
    
    print("\n" + "=" * 70)
