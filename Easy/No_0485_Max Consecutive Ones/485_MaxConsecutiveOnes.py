
#Runtime: 364 ms, faster than 93.87% of Python3 online submissions for Max Consecutive Ones.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones.

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ans = 0
        tmp = 0
        for n in nums:
            if n == 1:
                tmp += 1
            else: 
                if tmp > ans:
                    ans = tmp
                tmp = 0 #途切れたら初期化
        if tmp > ans: #連続が途切れずに終わった場合と、最後の連続が一番大きい場合
            return tmp
        else:
            return ans
