class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        # Time Complexity O(n^2)
        #Runtime: 508 ms, faster than 13.61% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
        #Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
        ans = []
        for i in range(len(nums)):
            tmp = 0
            for n in range(len(nums)):
                if nums[i] > nums[n] and i != n:
                    tmp += 1
            ans.append(tmp)

        return ans
        '''
        #Runtime: 84 ms, faster than 48.28% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
        #Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
        result = []
        if len(nums) == 0:
            return result
        
        nums_sort = sorted(nums)
        
        for val in nums:
            result.append(nums_sort.index(val))
        return result
        
