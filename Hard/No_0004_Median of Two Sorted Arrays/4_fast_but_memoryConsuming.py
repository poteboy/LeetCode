#Runtime: 80 ms, faster than 99.39% of Python3 online submissions for Median of Two Sorted Arrays.
#Memory Usage: 14 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if length % 2 != 0:
            return float(nums[length//2])
        else:
            index = length // 2
            return float((nums[index] + nums[index-1]) / 2)
        
