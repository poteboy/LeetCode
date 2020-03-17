class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        #Insert Sort
        for i in range(1, len(nums)):
            tmp = nums[i]
            for j in range( i-1 , -1 , -1):
                if tmp < nums[j]:
                    nums[j +1] = nums[j]
                else:
                    nums[j + 1] = tmp
                    break
            else:
                nums[0] = tmp
        '''
        #Selective Sort
        for n in range(0, len(nums) -1):
            tmp = n
            for i in range(n+1 , len(nums)):
                if nums[tmp] > nums[i]:
                    tmp = i
            nums[n],nums[tmp] = nums[tmp],nums[n]
        '''
                
                
