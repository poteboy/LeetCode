class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #ハッシュマップを使う方法
        #Runtime: 400 ms, faster than 49.49% of Python3 online submissions for Find All Numbers Disappeared in an Array.
        #Memory Usage: 24.8 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
        if nums == []:
            return []
        
        
        big = len(nums)
        hashmap = dict.fromkeys([i for i in range(1,big+1)], 0)
        for i in nums:
            hashmap[i] += 1
        ans = []
        n = 0
        for key,val in dict.items(hashmap):
            if hashmap[key] == 0:
                ans.append(key)
                n += 1
        return ans
        '''
        #集合演算を使う方法
        #Runtime: 368 ms, faster than 80.73% of Python3 online submissions for Find All Numbers Disappeared in an Array.
        #Memory Usage: 26.4 MB, less than 7.14% of Python3 online submissions for Find All Numbers
        a = {i for i in range(1, len(nums)+ 1)}
        b = set(nums)
        diff = a ^ b #^は共通しないもの（&は共通するもの）
        ans = sorted(list(diff))
        return ans
        '''
        
        
