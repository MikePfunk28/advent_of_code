from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        overall_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                overall_count = max(overall_count, count)
            else:
                # reset when we hit a zero
                count = 0
        # overall_count holds the maximum streak
        return overall_count
        
if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))