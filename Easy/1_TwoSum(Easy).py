# Time Complexity O(N^2)
# 要改善
from functools import lru_cache
from typing import Sequence


class Solution:
    def twoSum(self, nums: Sequence, target: int):
    
        num = set(nums)
        for i in num:
            for n in num:
                if i + n == target:
                    break
            else:
                continue
            break
        ans0 = nums.index(i)
        ans1 = nums.index(n)
        if ans0 == ans1:
            ans = [y for y, x in enumerate(nums) if x == i]
            if len(ans) == 2:
                return ans
        if ans0 > ans1:
            return [ans1, ans0]
        else:
            return [ans0, ans1]
