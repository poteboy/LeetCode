
#Runtime: 172 ms, faster than 86.23% of Python3 online submissions for Majority Element.
#Memory Usage: 14.2 MB, less than 97.62% of Python3 online submissions for Majority Element.
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums) / 2
        num = set(nums) #辞書に入れるために重複を消す

        hashmap =  {n:0 for n in num} #キーをnumにある数字、バリューを全て０にする
        for i in nums:
            hashmap[i] += 1 #重複の回数＋１する
        for key,val in hashmap.items():
            if val > size:
                break
        return key
