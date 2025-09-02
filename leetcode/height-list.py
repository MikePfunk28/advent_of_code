from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # calculate area with current pointers
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            max_area = max(max_area, area)

            # move pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))

# Couldnt we enumerate all the pairs and calculate the area?
# Yes, we could use a nested loop to check all pairs of lines.
# However, this would be less efficient than the two-pointer approach.
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i + 1:], i + 1):
                width = j - i
                current_height = min(h1, h2)
                area = width * current_height
                max_area = max(max_area, area)
        return max_area

if __name__ == "__main__":
    solution = Solution2()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))