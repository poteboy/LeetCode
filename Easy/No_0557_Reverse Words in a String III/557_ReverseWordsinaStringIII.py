
#Runtime: 32 ms, faster than 69.74% of Python3 online submissions for Reverse Words in a String III.
#Memory Usage: 13.2 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = []
        for word in s:
            word = word[::-1]
            ans.append(word)
        return ' '.join(ans)
        #別解
        #return return ' '.join([''.join(reversed(x)) for x in s.split()])
        
       
