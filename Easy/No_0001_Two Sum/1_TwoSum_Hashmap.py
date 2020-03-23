#リストのset化とほぼ計算量、メモリは同じ（むしろ少し負けてる）だが、こちらの方がスマートな解法である

# Time Complexity : O(N)
# Space Complexity : O(N)

#Runtime: 52 ms, faster than 54.83% of Python3 online submissions for Two Sum.
#Memory Usage: 14.2 MB, less than 54.65% of Python3 online submissions for Two Sum.

a = [2,7,11,15]
from typing import MutableSequence

class Solution:
    def twoSum(self, nums: MutableSequence, target: int):
        #hashmap = dict.fromkeys(nums, 0)
        ans = []
        hashmap = {}
        for key, val in enumerate(nums):
            #getは値が存在しない場合でもNoneを返してくれる。(hashmap[val]だと存在しない場合エラーになる)       
            if hashmap.get(val) is None:
                hashmap[target - val] = key
            else:
                ans = [hashmap[val], key]
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(a , 9))
