#Runtime: 56 ms, faster than 96.76% of Python3 online submissions for Two Sum II - Input array is sorted.
#Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict.fromkeys(numbers, None)
        for val, key in enumerate(numbers):
            if hashmap[key] == None:
                hashmap[target - key] = val
            else:
                return [hashmap[key] + 1, val + 1]
