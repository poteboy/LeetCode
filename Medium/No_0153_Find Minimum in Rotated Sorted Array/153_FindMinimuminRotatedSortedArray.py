#Runtime: 40 ms, faster than 59.04% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
#Memory Usage: 13.1 MB, less than 98.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid -1]: #左の数の方が大きかったら、midがpivot
                return nums[mid]
            elif nums[mid +1] < nums[mid]: #右の数が小さかったら、右がpivot
                return nums[mid + 1]
            elif nums[left] < nums[mid] and nums[mid] > nums[right]: #mid以前がソートされてたら、mid以降にpivotがあると踏む
                left = mid + 1
            else: #mid以降がソートされてたら、mid以前に問題があると踏む。
                right = mid -1
        else: #上の方法だと、はじめからソート済の配列ではNoneがでてしまうので、ここでその場合の数を返す。
            return nums[0]
            
            
#Runtime: 36 ms, faster than 83.75% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
#Memory Usage: 13.2 MB, less than 62.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.                 
            
  class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                return nums[0]
            elif mid > 0 and nums[mid] < nums[mid -1]:
                return nums[mid]
            elif nums[mid +1] < nums[mid]:
                return nums[mid + 1]
            elif nums[left] < nums[mid] and nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid -1
