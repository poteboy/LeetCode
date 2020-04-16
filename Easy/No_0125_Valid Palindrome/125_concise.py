#Runtime: 32 ms, faster than 97.74% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 19.6 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        return s == s[::-1]
