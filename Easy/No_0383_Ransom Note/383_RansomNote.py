#Runtime: 40 ms, faster than 83.23% of Python3 online submissions for Ransom Note.
#Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Ransom Note.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter 
        left = Counter(ransomNote)
        right = Counter(magazine)
        for i in left:
            if i not in right or left[i] > right[i]:
                return False 
        return True
        
