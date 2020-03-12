#最初と最後を入れ替える
#-iだと、-0になってしまうので、さらに-1する

#Runtime: 208 ms, faster than 85.14% of Python3 online submissions for Reverse String.
#Memory Usage: 17.3 MB, less than 97.67% of Python3 online submissions for Reverse String.

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) //2):
            s[i],s[-i-1] = s[-i-1],s[i]
        return
        
