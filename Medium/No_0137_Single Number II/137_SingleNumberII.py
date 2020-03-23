
#Runtime: 56 ms, faster than 78.46% of Python3 online submissions for Single Number II.
#Memory Usage: 14.8 MB, less than 40.00% of Python3 online submissions for Single Number II.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return ( (3* sum(set(nums))) - sum(nums)) // 2
        
