
#別解はかなり遅い上にspace complexityも悪い。
#等差数列の和を使う
# 1/2* 項数　* (初項　+ 末項)

#Runtime: 136 ms, faster than 84.43% of Python3 online submissions for Missing Number.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Missing Number.

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)*(len(nums)+1) // 2) - sum(nums)
'''
        if len(nums) == 1 and nums[0] == 0:
            return 1
        
        max_val = max(nums)
        hashmap = {i:0 for i in range(max_val+1)}

        for i in nums:
            hashmap[i] += 1
            
        ans = 0
        for key, val in hashmap.items():
            if val == 0:
                ans = key
                break
        else:
            return max_val + 1
        return ans
'''

if __name__ == '__main__':
    [9,6,4,2,3,5,7,0,1]
    s = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(s.missingNumber(nums))
