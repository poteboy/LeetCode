#Runtime: 40 ms, faster than 57.02% of Python3 online submissions for Permutations.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutations.

from typing import List
from itertools import permutations

class Solution:
    def permute(self,nums: List[int]) -> List[List[int]]:
        ans = []
        for i in permutations(nums):
            ans.append(list(i))
        return ans
    #後でライブラリを使用しない解答も考える（再帰）


if __name__ =='__main__':
    nums: List[int] = [None] * int(input('配列の個数：'))
    for n in range(len(nums)):
        nums[n] = int(input(f'{n +1}個目の要素'))
    s = Solution()
    print(*s.permute(nums), sep ='\n')

#*はアンパック（二次元配列）
