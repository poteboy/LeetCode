#Runtime: 32 ms, faster than 23.87% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 13.9 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.

#Time Complexity is O(n^2) due to the nested loops

class Solution:
    def generate(self, num):
        if num == 0: 
            return []
        ans = []
        for i in range(num):
            tmp = [None] * (i +1)
            tmp[0] = tmp[-1] = 1
            if i >= 2:
                for n in range(len(tmp)):
                    if tmp[n] == None:
                        tmp[n] = ans[i -1][n] + ans[i-1][n-1]
            ans.append(tmp)
        return ans 
        
