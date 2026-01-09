"""
SINGLY LINKED LIST - OPERATIONS
================================

Advanced operations on singly linked lists:
- Insert at specific position
- Delete from specific position
- Reverse the list
- Find middle element
"""

from typing import Optional


class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly linked list with advanced operations.
    """
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add element at the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, data, position):
        """
        Insert element at a specific position (0-indexed).
        Example: insert_at_position(25, 2) inserts 25 at index 2
        
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        # Insert at the beginning (position 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Find the node before the insertion point
        current = self.head
        for i in range(position - 1):
            if current is None:
                print(f"Position {position} is out of range!")
                return
            current = current.next
        
        # Insert the new node
        if current is None:
            print(f"Position {position} is out of range!")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self, position):
        """
        Delete element at a specific position (0-indexed).
        Example: delete_at_position(1) deletes the element at index 1
        
        Time Complexity: O(n)
        """
        if self.head is None:
            print("List is empty!")
            return
        
        # Delete from the beginning
        if position == 0:
            self.head = self.head.next
            return
        
        # Find the node before the one to delete
        current = self.head
        for i in range(position - 1):
            if current is None:
                print(f"Position {position} is out of range!")
                return
            current = current.next
        
        # Check if position exists and delete
        if current is None or current.next is None:
            print(f"Position {position} is out of range!")
            return
        
        current.next = current.next.next
    
    def reverse(self):
        """
        Reverse the linked list IN-PLACE.
        
        Before: 10 → 20 → 30 → None
        After:  30 → 20 → 10 → None
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        
        while current:
            # Store the next node temporarily
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move prev and current one step forward
            prev = current
            current = next_node
        
        # Update head to point to the new first node
        self.head = prev
    
    def find_middle(self) -> Optional[int]:
        """
        Find the middle element of the linked list using
        the "slow and fast pointer" technique.
        
        Slow pointer moves 1 step at a time
        Fast pointer moves 2 steps at a time
        When fast reaches end, slow is at middle
        
        Example: [10, 20, 30, 40, 50] → middle is 30
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        
        # Move fast by 2 steps and slow by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def display(self):
        """Print all elements in the list."""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" → ".join(elements) + " → None")


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("SINGLY LINKED LIST - ADVANCED OPERATIONS")
    print("=" * 70)
    
    # Create and populate the list
    ll = SinglyLinkedList()
    for val in [10, 20, 30, 40, 50]:
        ll.append(val)
    
    # 1. Display original list
    print("\n1. ORIGINAL LIST:")
    print("   ", end="")
    ll.display()
    
    # 2. Insert at specific positions
    print("\n2. INSERT AT SPECIFIC POSITIONS:")
    print("   Inserting 15 at position 1")
    ll.insert_at_position(15, 1)
    print("   ", end="")
    ll.display()
    
    print("   Inserting 25 at position 3")
    ll.insert_at_position(25, 3)
    print("   ", end="")
    ll.display()
    
    # 3. Find middle element
    print("\n3. FIND MIDDLE ELEMENT:")
    middle = ll.find_middle()
    print(f"   Middle element: {middle}")
    
    # 4. Delete from specific position
    print("\n4. DELETE AT SPECIFIC POSITIONS:")
    print("   Deleting element at position 2")
    ll.delete_at_position(2)
    print("   ", end="")
    ll.display()
    
    # 5. Reverse the list
    print("\n5. REVERSE THE LIST:")
    print("   Before reverse: ", end="")
    ll.display()
    
    ll.reverse()
    
    print("   After reverse:  ", end="")
    ll.display()
    
    print("\n" + "=" * 70)
