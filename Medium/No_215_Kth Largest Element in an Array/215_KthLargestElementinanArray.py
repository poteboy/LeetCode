#ヒープソート＋再帰を使った方法もあるのであとで復習する

#Runtime: 68 ms, faster than 57.03% of Python3 online submissions for Kth Largest Element in an Array.
#Memory Usage: 14 MB, less than 27.50% of Python3 online submissions for Kth Largest Element in an Array.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hashmap = dict.fromkeys(list(set(nums)), 0)

        for n in nums:
            hashmap[n] += 1

        ans = sorted(hashmap.items())

        k = k
        for i in range(len(ans)-1, -1, -1):
            if ans[i][1] - k >= 0:
                return ans[i][0]
                break
            else:
                k -= ans[i][1]
