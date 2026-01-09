class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices ={}
        for i,num in enumerate(nums):
            num2 = target - num
            if num2 in indices:
                return [indices[num2],i]
            indices[num]=i

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))  # Output: [0, 1]
    print(solution.twoSum([3,2,4], 6))      # Output: [1, 2]
    print(solution.twoSum([3,3], 6))        # Output: [0, 1]

#Time Complexity: O(n)
#Space Complexity: O(n)