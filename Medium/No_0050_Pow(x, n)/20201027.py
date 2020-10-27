from functools import lru_cache

class Solution:
    @lru_cache(maxsize=1000)
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        elif n == 0:
            return 1
        elif n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x, n/2) * self.myPow(x, n/2)

'''
計算量: O(log(n))
メモ化で計算速度を上げているので純粋なアルゴリズムで解けるようになりたい
'''