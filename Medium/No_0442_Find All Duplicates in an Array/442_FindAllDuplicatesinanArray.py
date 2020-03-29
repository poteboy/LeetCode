#問題文にはwithout extra space and in O(n) runtimeとあったので、２つ目の解き方はhashmapをつくり余計にメモリを食ってるから駄目。
#な筈なのだが制約通りの１つ目の解き方よりも性能が良い。しかもless complex。

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #Runtime: 400 ms, faster than 45.87% of Python3 online submissions for Find All Duplicates in an Array.
        #Memory Usage: 21.2 MB, less than 7.14% of Python3 online submissions for Find All Duplicates in an Array.
        ans = []
        for i in nums:
            if nums[abs(i) -1] < 0:
                ans.append(abs(i))
            else:
                nums[abs(i) -1] *= -1
        return ans
'''
#Runtime: 364 ms
#Memory Usage: 22.4 MB
#Time Complexity: O(n)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = dict.fromkeys(nums, 0)
        ans = []
        for i in nums:
            a[i] += 1
        for key, val in dict.items(a):
            if a[key] == 2:
                ans.append(key)
        return ans 
