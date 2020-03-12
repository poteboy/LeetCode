
#Binary Search
class Solution:
    from typing import Sequence
    def searchInsert(self, nums, target):
        ans = self.bin_search(nums, target)
        return ans


    def bin_search(self,a: Sequence, key:int):
        pl = 0
        pr = len(a) - 1
        while True:
            pc =  (pl + pr) // 2
            if a[pc] == key:
                return pc
            elif a[pc] < key:
                pl = pc +1
            else:
                pr = pc -1
            if pl > pr:
                return pl
