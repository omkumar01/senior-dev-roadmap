from typing import List

# ============================================================================
# SOLUTION 1: SLICING APPROACH
# ============================================================================
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate array to the right by k steps using slicing.
        
        Approach:
        - Extract the last k elements: nums[size - k:]
        - Extract the first (size - k) elements: nums[0:size - k]
        - Concatenate them to get rotated array
        - Use nums[:] to modify in-place
        
        Do not return anything, modify nums in-place instead.
        
        Time Complexity: O(n) - slicing creates new lists, concatenation traverses all elements
        Space Complexity: O(n) - temporary lists created during slicing and concatenation
        """
        size = len(nums)
        
        # Normalize k to avoid unnecessary rotations
        # If k > size, rotating by k is same as rotating by k % size
        if k > size:
            k = k % size
        
        # Slice and concatenate: move last k elements to front
        nums[:] = nums[size - k:] + nums[0:size - k]


# ============================================================================
# SOLUTION 2: REVERSAL APPROACH (OPTIMAL)
# ============================================================================
class SolutionOptimal:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate array to the right by k steps using reversal algorithm.
        
        Approach:
        Three reversals to achieve rotation:
        1. Reverse entire array
        2. Reverse first k elements
        3. Reverse remaining elements
        
        Example: nums = [1,2,3,4,5,6,7], k = 3
        - Reverse all: [7,6,5,4,3,2,1]
        - Reverse first 3: [5,6,7,4,3,2,1]
        - Reverse rest: [5,6,7,1,2,3,4] ✓
        
        Time Complexity: O(n) - three complete traversals
        Space Complexity: O(1) - only swaps, no extra space
        """
        size = len(nums)
        k = k % size
        
        def reverse(start: int, end: int) -> None:
            """Helper function to reverse array elements in-place."""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse entire array
        reverse(0, size - 1)
        
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse remaining elements
        reverse(k, size - 1)


# ============================================================================
# TEST CASES AND RESULTS
# ============================================================================
def test_solutions():
    """Test both solutions with various test cases."""
    
    test_cases = [
        # (nums, k, expected_output)
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1], 0, [1]),
        ([1, 2], 1, [2, 1]),
        ([1, 2], 3, [2, 1]),  # k > size
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),  # k = 0
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # k = size
        (list(range(1, 11)), 7, [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]),
    ]
    
    sol1 = Solution()
    sol2 = SolutionOptimal()
    
    print("=" * 70)
    print("TESTING ROTATE ARRAY SOLUTIONS")
    print("=" * 70)
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # Test Solution 1
        test_nums1 = nums.copy()
        sol1.rotate(test_nums1, k)
        result1 = "✓ PASS" if test_nums1 == expected else "✗ FAIL"
        
        # Test Solution 2
        test_nums2 = nums.copy()
        sol2.rotate(test_nums2, k)
        result2 = "✓ PASS" if test_nums2 == expected else "✗ FAIL"
        
        print(f"\nTest Case {i}:")
        print(f"  Input:    nums = {nums}, k = {k}")
        print(f"  Expected: {expected}")
        print(f"  Solution 1 (Slicing):  {test_nums1} - {result1}")
        print(f"  Solution 2 (Reversal): {test_nums2} - {result2}")
    
    print("\n" + "=" * 70)
    print("COMPLEXITY COMPARISON")
    print("=" * 70)
    print(f"{'Approach':<20} {'Time':<15} {'Space':<15}")
    print("-" * 70)
    print(f"{'Slicing':<20} {'O(n)':<15} {'O(n)':<15}")
    print(f"{'Reversal (Optimal)':<20} {'O(n)':<15} {'O(1)':<15}")
    print("=" * 70)


if __name__ == "__main__":
    test_solutions()