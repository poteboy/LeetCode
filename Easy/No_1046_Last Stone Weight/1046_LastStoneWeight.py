#Runtime: 32 ms, faster than 42.35% of Python3 online submissions for Last Stone Weight.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >1:
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            dif = abs(x -y)
            stones.append(dif)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
