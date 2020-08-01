from math import floor

# Runtime: 2232 ms, faster than 8.27% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.6 MB, less than 94.24% of Python3 online submissions for Sqrt(x).
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1, x+2):
	        if i*i > x:
		        return i-1

# memory exceeded 
class Solution2:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        arr = [int(i+1) for i in range(x)]
        left = 1
        right = x
        while left < right:
            mid = left  + floor((right - left)//2)
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid
            elif mid ** 2 < x:
                left  = mid + 1

        return left -1

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(2147395599))