
#恐らくLeetcode史上一番簡単な問題。
#Time Complexity O(logN)以下で探せ（それでも２分探索を使えばいいだけなので超簡単だが）でもなく、なんの指示もない。
#現にLinear Searchでやっても91％のpythonユーザーより早いRun timeになった。

#Runtime: 48 ms, faster than 91.00% of Python3 online submissions for Search in Rotated Sorted Array II.
#Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array II.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in nums:
            if i == target:
                return True
        else:
            return False
