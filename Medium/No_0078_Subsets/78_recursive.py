class Solution(object):
    def subset(self, nums):
        ans = []
        def helper(nums, ans, curr, index):
            #下でcurrをリスト化しなければならない理由は、例えappendしたとしたもansの中でappendされたcurrは更新され続けるから
            ans.append(list(curr))
            for i in range(index, len(nums)):
                curr.append(nums[i])
                helper(nums, ans, curr, i+1)
                curr.pop()

        helper(nums, ans,[], 0)
        return ans 


s = Solution()
print(s.subset([1,2,3]))
