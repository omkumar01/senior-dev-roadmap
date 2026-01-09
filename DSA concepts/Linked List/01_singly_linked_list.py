"""
SINGLY LINKED LIST - Basic Implementation
==========================================

A singly linked list is a linear data structure where each node contains:
- Data: The value stored in the node
- Next: A reference/pointer to the next node

Example: [10 → 20 → 30 → 40 → None]
"""


class Node:
    """
    Represents a single node in the linked list.
    
    Attributes:
        data: The value to store in this node
        next: Reference to the next node (initially None)
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    A singly linked list implementation with basic operations.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def append(self, data):
        """
        Add a node with data to the end of the list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        # If list is empty, make new node as head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Add new node at the end
        current.next = new_node
    
    def prepend(self, data):
        """
        Add a node with data at the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        """Print all elements in the list."""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        # Print in format: 10 → 20 → 30 → None
        print(" → ".join(elements) + " → None")
    
    def search(self, target):
        """
        Search for a value in the list.
        Returns True if found, False otherwise.
        Time Complexity: O(n)
        """
        current = self.head
        
        while current:
            if current.data == target:
                return True
            current = current.next
        
        return False
    
    def get_length(self):
        """
        Get the number of nodes in the list.
        Time Complexity: O(n)
        """
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
    print("=" * 60)
    print("SINGLY LINKED LIST - BASIC OPERATIONS")
    print("=" * 60)
    
    # Create a new linked list
    linked_list = SinglyLinkedList()
    
    # 1. Add elements using append (adds to the end)
    print("\n1. Adding elements: 10, 20, 30, 40 (using append)")
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    
    print("   Linked List: ", end="")
    linked_list.display()
    
    # 2. Add element at the beginning using prepend
    print("\n2. Adding 5 at the beginning (using prepend)")
    linked_list.prepend(5)
    print("   Linked List: ", end="")
    linked_list.display()
    
    # 3. Get the length of the list
    print("\n3. Length of the list:", linked_list.get_length())
    
    # 4. Search for elements
    print("\n4. Searching for elements:")
    print(f"   Is 30 in the list? {linked_list.search(30)}")  # True
    print(f"   Is 100 in the list? {linked_list.search(100)}")  # False
    
    # 5. Display the final list
    print("\n5. Final Linked List: ", end="")
    linked_list.display()
    
    print("\n" + "=" * 60)
