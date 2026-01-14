"""
Reverse Integer Problem - LeetCode

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing causes overflow, return 0.

32-bit signed integer range: [-2^31, 2^31 - 1] = [-2147483648, 2147483647]
"""


class Solution:
    def reverse_string_approach(self, x: int) -> int:
        """
        Solution 1: String Conversion Approach (Optimal)
        
        Approach: Convert to string, reverse, and convert back to integer.
        This approach is simple and leverages Python's built-in reverse.
        
        Time Complexity: O(log n) where n is the number, since a 32-bit int
                         has at most ~10 digits. Converting to string, reversing,
                         and converting back all take O(log n) time.
        
        Space Complexity: O(log n) for storing the reversed string representation
        
        Advantage: Clean and concise code
        Disadvantage: Uses string conversion which may not be allowed in some languages
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle zero case
        if x == 0:
            return 0
        
        # Extract sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Convert to string, reverse it, and convert back with sign
        reversed_num = int(str(x)[::-1]) * sign
        
        # Check for 32-bit overflow
        if reversed_num <= INT_MIN or reversed_num >= INT_MAX:
            return 0
        
        return reversed_num
    
    def reverse_math_approach(self, x: int) -> int:
        """
        Solution 2: Mathematical/Pop-and-Push Approach
        
        Approach: Repeatedly pop the last digit and build the reversed number
        without using string conversion. This approach works across all languages.
        
        Time Complexity: O(log n) where n is the number (same as string approach)
        
        Space Complexity: O(1) - only using a few variables for computation
        
        Advantage: Language-independent, no string conversion needed
        Disadvantage: Slightly more complex logic
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        reversed_num = 0
        x_copy = x
        
        # Extract and reverse digits
        while x_copy != 0:
            # Extract last digit
            digit = x_copy % 10
            
            # Handle negative numbers: adjust digit extraction
            if x_copy < 0 and digit != 0:
                digit -= 10
                x_copy = -((-x_copy) // 10)
            else:
                x_copy //= 10
            
            # Check overflow before pushing the digit
            # If reversed_num > INT_MAX // 10, overflow is guaranteed
            # If reversed_num == INT_MAX // 10, check if digit > 7 (last digit of INT_MAX)
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0
            
            # If reversed_num < INT_MIN // 10, overflow for negative
            # If reversed_num == INT_MIN // 10, check if digit < -8 (last digit of INT_MIN)
            if reversed_num < INT_MIN // 10 or (reversed_num == INT_MIN // 10 and digit < -8):
                return 0
            
            # Push digit to reversed number
            reversed_num = reversed_num * 10 + digit
        
        return reversed_num
    
    def reverse_cleaner_math_approach(self, x: int) -> int:
        """
        Solution 3: Simplified Mathematical Approach
        
        Approach: Use modulo to extract digits and handle sign separately.
        Similar to Solution 2 but cleaner implementation.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Advantage: Cleaner than Solution 2, still language-independent
        Disadvantage: Works well for Python, less portable than Solution 2
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Extract sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        
        # Build reversed number digit by digit
        while x:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Apply sign
        reversed_num *= sign
        
        # Clamp to 32-bit range
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        
        return reversed_num
    
    # Keep the original method as the main solution
    def reverse(self, x: int) -> int:
        """Main solution - uses string conversion approach"""
        return self.reverse_string_approach(x)


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Comprehensive test cases for all three approaches"""
    solution = Solution()
    
    # Test cases: (input, expected_output, description)
    test_cases = [
        (123, 321, "Basic positive number"),
        (-123, -321, "Basic negative number"),
        (120, 21, "Number with trailing zero"),
        (0, 0, "Zero"),
        (1534236469, 0, "Overflow case - larger than INT_MAX"),
        (-2147483648, 0, "INT_MIN - causes overflow when reversed"),
        (1, 1, "Single digit"),
        (-1, -1, "Single digit negative"),
        (10, 1, "Number ending with zero"),
        (100, 1, "Multiple trailing zeros"),
        (2147483647, 0, "INT_MAX - causes overflow when reversed"),
        (1534236467, 7646324351, "Large number (would overflow if unchecked)"),
    ]
    
    approaches = [
        ("String Approach", solution.reverse_string_approach),
        ("Math Approach", solution.reverse_math_approach),
        ("Cleaner Math Approach", solution.reverse_cleaner_math_approach),
    ]
    
    print("=" * 80)
    print("REVERSE INTEGER - TEST RESULTS")
    print("=" * 80)
    
    for approach_name, method in approaches:
        print(f"\n{approach_name}:")
        print("-" * 80)
        passed = 0
        failed = 0
        
        for input_val, expected, description in test_cases:
            result = method(input_val)
            status = "✓ PASS" if result == expected else "✗ FAIL"
            
            if result == expected:
                passed += 1
            else:
                failed += 1
            
            print(f"{status} | Input: {input_val:>11} | Expected: {expected:>11} | Got: {result:>11} | {description}")
        
        print("-" * 80)
        print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests\n")


if __name__ == "__main__":
    run_tests()