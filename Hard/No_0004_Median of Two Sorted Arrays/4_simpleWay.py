
#Runtime: 92 ms, faster than 81.63% of Python3 online submissions for Median of Two Sorted Arrays.
#Memory Usage: 14.1 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 1:
            index = len(nums) // 2
            return float(nums[index])
        else:
            index2 = len(nums) // 2
            index1 = index2 - 1
            return float((nums[index1] + nums[index2]) /2)
        
