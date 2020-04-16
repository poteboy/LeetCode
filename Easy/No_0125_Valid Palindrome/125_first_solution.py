#Runtime: 56 ms, faster than 28.80% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 14.4 MB, less than 38.09% of Python3 online submissions for Valid Palindrome.

#　文字列.isalnum は、文字列が英数字のみで構成されていたらTrueを返す。
# 文字列.lower は文字列を小文字化するが、　文字列.islower　は文字列が小文字で構成されているか調べる

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        tmp = ''
        while True:
            if i >= len(s):
                break
            elif s[i].isalnum() is False:
                pass
            elif s[i].isalnum() is True:
                tmp += s[i]
            i += 1
        ans = tmp.lower()

        return ans == ans[::-1]
