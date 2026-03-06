from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(len(nums) // 2):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.shuffle([2,5,1,3,4,7], 3))