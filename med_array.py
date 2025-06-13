from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Median of two arrays.  So we need to sort and then the best for a sorted array is
        quicksort?
        """
        self.nums1 = nums1
        self.nums2 = nums2
        nums3 = nums1 + nums2
        nums3.sort()
        print(nums3)

        index_low = 0
        index_high = len(nums3) - 1

        while index_low <= index_high:
            index_med = (index_low + index_high) // 2
            guess = nums3[index_med]
            if (index_high + 1) % 2 == 0:
                return (nums3[index_med] + nums3[index_med + 1]) / 2
            else:
                return nums3[index_med]


mysolution = Solution()
print(mysolution.findMedianSortedArrays([1, 5,9,8,3], [2,4,6]))  # Output: 2.00000