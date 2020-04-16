#Runtime: 476 ms, faster than 16.98% of Python3 online submissions for Permutations II.
#Memory Usage: 14.2 MB, less than 6.67% of Python3 online submissions for Permutations II.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            ans = []
            for i in range(len(nums)):
                x = nums[i]
                y = nums[:i] + nums[i+1:]
                for j in self.permuteUnique(y):
                    tmp = [x] + j
                    if tmp in ans:
                        pass
                    else:
                        ans.append(tmp)
            return ans
