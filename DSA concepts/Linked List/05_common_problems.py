"""
COMMON LINKED LIST PROBLEMS
============================

Real-world problems and solutions using linked lists.
Great for practice and interviews!
"""

from typing import Optional


class Node:
    """Node for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListProblems:
    """
    Collection of common linked list problems with solutions.
    """
    
    @staticmethod
    def create_linked_list(values):
        """Helper function to create a linked list from a list of values."""
        if not values:
            return None
        head = Node(values[0])
        current = head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next
        return head
    
    @staticmethod
    def display_list(head):
        """Helper function to display a linked list."""
        elements = []
        current = head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " → ".join(elements) + " → None"
    
    # =====================================================================
    # PROBLEM 1: REMOVE DUPLICATES
    # =====================================================================
    
    @staticmethod
    def remove_duplicates(head) -> Optional[Node]:
        """
        Remove duplicate values from a sorted linked list.
        
        Example:
            Input:  1 → 1 → 2 → 3 → 3 → 3 → 4
            Output: 1 → 2 → 3 → 4
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None:
            return head
        
        current = head
        
        while current and current.next:
            # If current and next have the same data
            if current.data == current.next.data:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to next node
                current = current.next
        
        return head
    
    # =====================================================================
    # PROBLEM 2: FIND NTH NODE FROM END
    # =====================================================================
    
    @staticmethod
    def find_nth_from_end(head, n) -> Optional[int]:
        """
        Find the value of the nth node from the end.
        
        Example:
            List: 1 → 2 → 3 → 4 → 5
            n = 2: Returns 4 (2nd node from end is 4)
        
        Technique: Two-pointer approach (slow & fast)
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None:
            return None
        
        # Create two pointers, n steps apart
        fast = head
        slow = head
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            if fast is None:
                return None  # n is larger than list length
            fast = fast.next
        
        # Move both pointers until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next
        
        return slow.data if slow else None
    
    # =====================================================================
    # PROBLEM 3: DETECT CYCLE
    # =====================================================================
    
    @staticmethod
    def has_cycle(head) -> bool:
        """
        Detect if a linked list has a cycle (circular reference).
        
        Technique: Floyd's cycle detection algorithm (tortoise and hare)
        - Slow pointer moves 1 step
        - Fast pointer moves 2 steps
        - If they meet, there's a cycle
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there's a cycle
            if slow == fast:
                return True
        
        return False
    
    # =====================================================================
    # PROBLEM 4: MERGE TWO SORTED LISTS
    # =====================================================================
    
    @staticmethod
    def merge_sorted_lists(l1, l2) -> Optional[Node]:
        """
        Merge two sorted linked lists into one sorted list.
        
        Example:
            List1: 1 → 3 → 5
            List2: 2 → 4 → 6
            Output: 1 → 2 → 3 → 4 → 5 → 6
        
        Time Complexity: O(n + m) where n and m are list lengths
        Space Complexity: O(1)
        """
        # Create a dummy node to simplify the logic
        dummy = Node(0)
        current = dummy
        
        # Traverse both lists and add smaller element to result
        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Add remaining elements
        if l1:
            current.next = l1
        else:
            current.next = l2
        
        return dummy.next
    
    # =====================================================================
    # PROBLEM 5: ROTATE LIST
    # =====================================================================
    
    @staticmethod
    def rotate_list(head, k) -> Optional[Node]:
        """
        Rotate the list k steps to the right.
        
        Example:
            List: 1 → 2 → 3 → 4 → 5
            k = 2: Returns 4 → 5 → 1 → 2 → 3
        
        Algorithm:
            1. Find the length of the list
            2. Normalize k (k = k % length)
            3. Find the new head position
            4. Connect the tail to the original head to form a circle
            5. Break the circle at the new position
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or k == 0:
            return head
        
        # Find length and get the last node
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        
        # Normalize k
        k = k % length
        if k == 0:
            return head
        
        # Make the list circular
        current.next = head
        
        # Find the new head (length - k steps from original head)
        steps_to_new_head = length - k
        current = head
        for _ in range(steps_to_new_head - 1):
            current = current.next
        
        # Break the circle
        new_head = current.next
        current.next = None
        
        return new_head


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("COMMON LINKED LIST PROBLEMS - SOLUTIONS")
    print("=" * 70)
    
    problems = LinkedListProblems()
    
    # PROBLEM 1: Remove Duplicates
    print("\n1. REMOVE DUPLICATES FROM SORTED LIST:")
    head1 = problems.create_linked_list([1, 1, 2, 3, 3, 3, 4])
    print(f"   Input:  {problems.display_list(head1)}")
    head1 = problems.remove_duplicates(head1)
    print(f"   Output: {problems.display_list(head1)}")
    
    # PROBLEM 2: Find Nth Node from End
    print("\n2. FIND NTH NODE FROM END:")
    head2 = problems.create_linked_list([1, 2, 3, 4, 5])
    print(f"   List:   {problems.display_list(head2)}")
    
    for n in [1, 2, 4]:
        result = problems.find_nth_from_end(head2, n)
        print(f"   Node {n} from end: {result}")
    
    # PROBLEM 3: Detect Cycle
    print("\n3. DETECT CYCLE IN LINKED LIST:")
    
    # Create a list without cycle
    head3a = problems.create_linked_list([1, 2, 3, 4, 5])
    print(f"   List without cycle: {problems.display_list(head3a)}")
    print(f"   Has cycle? {problems.has_cycle(head3a)}")
    
    # Create a list WITH cycle (manually)
    head3b = problems.create_linked_list([1, 2, 3, 4, 5])
    tail = head3b
    while tail.next:
        tail = tail.next
    tail.next = head3b.next  # Create cycle: 5 -> 2
    print(f"   List with cycle (1 → 2 → 3 → 4 → 5 → 2): ")
    print(f"   Has cycle? {problems.has_cycle(head3b)}")
    
    # PROBLEM 4: Merge Two Sorted Lists
    print("\n4. MERGE TWO SORTED LISTS:")
    l1 = problems.create_linked_list([1, 3, 5, 7])
    l2 = problems.create_linked_list([2, 4, 6, 8])
    print(f"   List 1: {problems.display_list(l1)}")
    print(f"   List 2: {problems.display_list(l2)}")
    merged = problems.merge_sorted_lists(l1, l2)
    print(f"   Merged: {problems.display_list(merged)}")
    
    # PROBLEM 5: Rotate List
    print("\n5. ROTATE LIST BY K STEPS:")
    head5 = problems.create_linked_list([1, 2, 3, 4, 5])
    print(f"   Original: {problems.display_list(head5)}")
    
    for k in [1, 2, 7]:
        head5 = problems.create_linked_list([1, 2, 3, 4, 5])
        rotated = problems.rotate_list(head5, k)
        print(f"   Rotated by {k}: {problems.display_list(rotated)}")
    
    print("\n" + "=" * 70)
