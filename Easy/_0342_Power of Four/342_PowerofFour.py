#２進法を使って解くらしい。２進法要勉強。

#Runtime: 68 ms, faster than 5.40% of Python3 online submissions for Power of Four.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Power of Four.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        ans = 4
        def check(num, ans):
            if num == ans:
                return True
            elif num > ans:
                ans *= 4
                return check(num, ans)
            elif num < ans:
                return False
        return check(num, ans)
        
