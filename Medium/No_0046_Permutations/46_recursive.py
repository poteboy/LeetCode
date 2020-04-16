
#Runtime: 40 ms, faster than 59.81% of Python3 online submissions for Permutations.
#Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        else:
            lst = []
            for i in range(len(nums)):
                x = nums[i]
                y = nums[:i] + nums[i+1:]
                for j in self.permute(y):
                    lst.append([x] + j)
            return lst
