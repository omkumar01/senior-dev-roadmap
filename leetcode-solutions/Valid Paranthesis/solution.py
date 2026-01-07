class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(','}':'{',']':'['}
        stack =[]
        for bracket in s:
            if bracket in bracket_map:
                if not stack or stack[-1] != bracket_map[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return len(stack)==0

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    
    for s, expected in test_cases:
        result = solution.isValid(s)
        assert result == expected, f"For input {s}, expected {expected} but got {result}"
    print("All test cases passed!")