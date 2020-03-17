
#Runtime: 24 ms, faster than 84.14% of Python3 online submissions for Guess Number Higher or Lower.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower.



# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while True:
            mid = (left + right) // 2
            tmp = guess(mid)
            if tmp == -1:
                right = mid -1 #一度当てはまらなかった数字は二度と当てはまることはない
            if tmp == 1:
                left = mid +1
            if tmp == 0:
                return mid
                
