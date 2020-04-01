#Runtime: 32 ms, faster than 19.54% of Python3 online submissions for Number Complement.
#Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Number Complement.


class Solution:
    def findComplement(self, num: int) -> int:
        def dec2bin(target):
            remainder = []
            while target != 0:
                remainder.append(str(target % 2))
                target = target // 2

            remainder.reverse()
            return remainder

        def bin2dec(target):
            n = len(target)-1 #指数の最大値
            sum = 0
            for i in range(len(target)):
                sum += (2 ** n) * int(target[i])
                n -= 1
            return sum
        
        def flip(target):
            ans = []
            for i in target:
                if i == '1':
                    ans.append('0')
                else:
                    ans.append('1')
            return int(''.join(ans))
        
        return bin2dec(str(flip(''.join(dec2bin(num)))))
        
