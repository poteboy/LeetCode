
#Runtime: 32 ms, faster than 66.63% of Python3 online submissions for Happy Number.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Happy Number.


import sys #再帰の上限を変更
sys.setrecursionlimit(50) #今回は深さの上限が５０で足りたが、場合によってはこれより多いかもしれない。
class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = 0
        for i in str(n):
            tmp += (int(i) **2)
        if tmp == 1:
            return True
        else:
            try:
                return self.isHappy(tmp)
            except RuntimeError: #再帰回数が５０を超えるとruntimerrorが出るので、その場合はfalseを返す。
                return False 
