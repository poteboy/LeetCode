#Runtime: 36 ms, faster than 32.26% of Python3 online submissions for Subsets.
#Memory Usage: 14.1 MB, less than 5.95% of Python3 online submissions for Subsets.


#このやり方はitertoolsを使ってるからコーディング面接では使えない。
#itertoolsのcombinationsは引数に配列と、組み合わせの範囲を取り、組み合わせを作成する。
#nums = [1,2,3]の例で言うと下のようになる。
#[[]]
#[[], [1]]
#[[], [1], [2]]
#[[], [1], [2], [3]]
#[[], [1], [2], [3], [1, 2]]
#[[], [1], [2], [3], [1, 2], [1, 3]]
#[[], [1], [2], [3], [1, 2], [1, 3], [2, 3]]
#[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
#[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]


from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = 0
        def helper(nums, ans, tmp):
            if tmp > len(nums):
                return 
            for i in combinations(nums, tmp):
                ans.append(list(i))
            helper(nums, ans, tmp+1)
        helper(nums, ans, tmp)
        return ans
        
   
