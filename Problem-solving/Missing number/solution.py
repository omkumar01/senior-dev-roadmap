"""
Simple Solution: Find Missing Number using Sum Method

This approach calculates the expected sum of numbers from 1 to n
and subtracts the actual sum of the array to find the missing number.
"""

def find_missing_number(arr):
    """
    Find the missing number in an unsorted array containing 1 to n natural numbers.
    
    Args:
        arr: List of integers containing n-1 numbers from range [1, n]
    
    Returns:
        int: The missing number
    """
    n = len(arr) + 1  # Actual range is 1 to n
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of array elements
    actual_sum = sum(arr)
    
    # The difference is the missing number
    missing = expected_sum - actual_sum
    
    return missing


# Test cases
if __name__ == "__main__":
    # Test 1
    arr1 = [1, 2, 4, 5]
    print(f"Input: {arr1}")
    print(f"Output: {find_missing_number(arr1)}")  # Expected: 3
    
    # Test 2
    arr2 = [3, 1, 2, 6, 4]
    print(f"\nInput: {arr2}")
    print(f"Output: {find_missing_number(arr2)}")  # Expected: 5
    
    # Test 3
    arr3 = [2, 4, 6, 7, 8]
    print(f"\nInput: {arr3}")
    print(f"Output: {find_missing_number(arr3)}")  # Expected: 1
    
    # Test 4
    arr4 = [1]
    print(f"\nInput: {arr4}")
    print(f"Output: {find_missing_number(arr4)}")  # Expected: 2


"""
COMPLEXITY ANALYSIS
====================

Time Complexity: O(n)
    - We iterate through the array once to calculate the sum
    - Mathematical calculations (n*(n+1)//2) are O(1)
    - Overall: O(n) where n is the length of the array

Space Complexity: O(1)
    - We only use a constant amount of extra space
    - No additional data structures are used
    - Only a few variables (expected_sum, actual_sum, missing) are stored
"""
