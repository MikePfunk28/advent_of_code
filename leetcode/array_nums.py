from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

if __name__ == "__main__":
    s = Solution()
    print(s.getConcatenation([1, 2, 1]))