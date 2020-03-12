#同じ重複が２つ以上含まれてはいけない、という問題を、全体のなかで重複が２つより多く存在してはいけない、だと勘違いしたため解くのに時間がかかった。
#実際の難易度的にはEasyレベル

#Runtime: 52 ms, faster than 80.38% of Python3 online submissions for Remove Duplicates from Sorted Array II.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array II.

class Solution:
    def removeDuplicates(self, nums) -> int: 
        #tmp = set(nums)
        hashmap = dict.fromkeys(nums, 0) #辞書をつくり何がどれだけ重複しているのか調べる
        for n in nums:
            hashmap[n] += 1 #valueには重複回数が入る

        tmp = 0
        for key, val in hashmap.items():
            if val > 2:
                tmp = val -2 
                #２回以上重複してる場合はそれを消せばい。
                #remove()メソッドは幸い最初に現れた指定した引数しか消さないためその利点をいかしてループで重複回数削除。
                for _ in range(tmp):
                    nums.remove(key)
            else:
                pass
        return len(nums)
    


s = Solution()
test = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(test ))
