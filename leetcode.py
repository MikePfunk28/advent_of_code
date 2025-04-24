# Two Sum
from typing import List

# Dealing with the typing here is the most annoying ever.
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """My first solution below is basically the
        brute force solution.  The fastest solution
        is apparently this one.  Where you are using
        a hash table or a dictionary to store the numbers."""
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
    # If no solution is found (shouldn't happen per problem statement)
        return []

    # First Attempt, just a brute force approach.
    def two_sums(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Test it
mysolution = Solution()
result = mysolution.two_sum(
    [2, 7, 4, 1, 8, 3, 5, 6, 2, 1, 4, 1, 5, 2, 9, 4, 8, 6, 7, 3, 11, 15], 9)

result = mysolution.two_sum(
    [2, 7, 11, 15, 8, 3, 5, 6, 2, 1, 5, 2, 9, 4, 8], 9)

result = mysolution.two_sum([2, 7, 11,  5, 6, 2, 1, 5, 2, 9, 15], 9)
print(result)

