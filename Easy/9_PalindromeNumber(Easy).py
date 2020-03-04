#Runtime 84 ms
#Memory 12.7 MB

from functools import reduce 
class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = ''
        a = [int(x) for x in list(str(x))]
        a.reverse()
        for i in range(len(a)):
            ans += str(a[i])
        ans = int(ans)
        if ans == x:
            return True
        else:
            return False

