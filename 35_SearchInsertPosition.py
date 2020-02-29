'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
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
