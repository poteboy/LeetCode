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
