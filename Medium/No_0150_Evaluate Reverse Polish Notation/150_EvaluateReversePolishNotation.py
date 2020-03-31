#Runtime: 72 ms, faster than 31.28% of Python3 online submissions for Evaluate Reverse Polish Notation.
#Memory Usage: 14 MB, less than 8.70% of Python3 online submissions for Evaluate Reverse Polish Notation.


from collections import deque
from typing import List
import math #floor切り捨て ceil切り上げ
class Solution:
    def evalRPN(self, tokens: List[str]):
        d = deque()
        for i in tokens:
            if i == '+':
                tmpA = int(d.pop())
                tmpB = int(d.pop())
                d.append(str(tmpA + tmpB))
                continue
            if i == '-':
                tmpA = int(d.pop())
                tmpB = int(d.pop())
                d.append(str(tmpB - tmpA))
                continue
            if i == '*':
                tmpA = int(d.pop())
                tmpB = int(d.pop())
                d.append(str(tmpA * tmpB))
                continue
            if i == '/':
                tmpA = int(d.pop())
                tmpB = int(d.pop())
                # 6 / - 132などの計算が何故か-1になるため（０より下は恐らく切り捨てと切り上げが反転する）
                if tmpB * tmpA < 0 and tmpB % tmpA != 0:
                    d.append(str(tmpB//tmpA+1))
                    continue
                d.append(str(tmpB//tmpA))
                continue
            else:
                d.append(i)
        return int(d.pop())

'''
今回は使わなかったが、eval()関数という便利な関数がある
例えば
eval('1 + 1')
をすると数値型で2が返ってくる。
引数は必ずstr型でなければならない点に注意
'''
