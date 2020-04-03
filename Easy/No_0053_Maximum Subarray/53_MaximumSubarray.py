
#Runtime: 68 ms, faster than 58.67% of Python3 online submissions for Maximum Subarray.
#Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.

# Linear Time Complexity  O(n)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
        

