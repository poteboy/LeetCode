#リストの末尾にNoneを追加し、それに出くわすまでループで０をNoneの右側に移す。

#Runtime: 52 ms, faster than 46.33% of Python3 online submissions for Move Zeroes.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.

from typing import List

class Solution:
    def moveZeroes(self,nums: List[int]) -> None:
        nums.append(None) 
        #[0, 1, 0, 3, 12, None]

        i = 0
        while nums[i] != None:
            if nums[i] == None:
                break
            if nums[i] == 0:
                tmp = nums.pop(i)
                nums.append(tmp)
            elif nums[i] != 0:
                i += 1

        nums.remove(None)
        return nums
    
    '''
    もっと簡単なやり方
    for _ in range(nums.count(0)): #countで指定した要素が何個あるか調べる
            nums.append(0)
            nums.remove(0)
        return nums
    '''

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    s = Solution()
    print(s.moveZeroes(nums))
