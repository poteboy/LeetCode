class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #改行する際はバックスラッシュを行末に置く
        return [
            'FizzBuzz' if i % 15 == 0 else\
            'Fizz' if i % 3 == 0 else \
            'Buzz' if i % 5 == 0 else str(i) for i in range(1,n+1)\
        ]
        
