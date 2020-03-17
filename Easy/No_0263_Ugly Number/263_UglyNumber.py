
#Runtime: 24 ms, faster than 93.49% of Python3 online submissions for Ugly Number.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Ugly Number.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        
        divide = [2,3,5]
        
        for n in divide:
            while True:
                if num % n == 0:
                    num = num // n
                else:
                    break
        if num == 1:
            return True
        else:
            return False
        '''
        while True:
            if num % 2 == 0:
                num = num // 2
                continue
            if num % 3 == 0:
                num = num // 3
                continue
            if num % 5 == 0:
                num = num// 5
                continue
            if num == 1:
                return True
            else:
                return False
        else:
            return False
        '''
                
