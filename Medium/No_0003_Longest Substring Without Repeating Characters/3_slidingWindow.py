class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case
        if s  == '':
            return 0
        if len(s) == 1:
            return 1
        
        hashmap = {}
        curr_sub_start = curr_len = ans = 0
        
        for i, letter in enumerate(s):
            if letter in hashmap and hashmap[letter] >= curr_sub_start:
                curr_sub_start = hashmap[letter] + 1
                curr_len = i - hashmap[letter] 
                hashmap[letter] = i
                
            else:
                hashmap[letter] = i
                curr_len += 1
                if curr_len > ans:
                    ans = curr_len
        return ans 
        
