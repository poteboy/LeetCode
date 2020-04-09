#解法１

#Runtime: 68 ms, faster than 62.38% of Python3 online submissions for Find the Duplicate Number.
#Memory Usage: 17.9 MB, less than 7.14% of Python3 online submissions for Find the Duplicate Number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set(nums)
        length_a = len(a)
        length_b = len(nums)
        a = sum(a)
        b = sum(nums)
        dist = length_b - length_a

        return  (b -a) // dist   
        
#解法２
＃Run Time: 72 ms
#Memory Usage: 17.2MB

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1).pop()[0]
