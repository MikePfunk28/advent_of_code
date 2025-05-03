from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """_summary_

        Args:
            nums1 (List[int]): _description_
            nums2 (List[int]): _description_

        Returns:
            float: _description_
        """
        # Initialize arrays and count just in case.
        self.nums1 = nums1
        self.nums2 = nums2
        self.count = 0
        # Call extend arr to add the arr to aar1, at the end.
        self.extend_arr(self.nums1, self.nums2)
        # Now sort the merged array.
        merged = sorted(self.nums1)
        # Define the Partition point.
        # If the length of the merged array is even, 
        # return the average of the two middle elements.
        # if odd return the middle element, or at position
        # of mid or median.
        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return merged[mid]

    def extend_arr(self, arr1, arr2):
        """_summary_

        Args:
            arr1 (_type_): _description_
            arr2 (_type_): _description_
        """
        # extend arr1 with arr2
        arr1.extend(arr2)
        print(arr1)

        return arr1


# sample data
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1, 2,3] and median is 2.
nums1 = [1, 4, 7, 6, 2, 3, 5]
nums2 = [9, 3, 7, 3, 3, 8, 6]
mysolution = Solution()

print(mysolution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.00000
# Output: [1, 4, 7, 6, 2, 3, 5, 9, 3, 7, 3, 3, 8, 6]
print(mysolution.add_arr(mysolution.nums1, mysolution.nums2))
