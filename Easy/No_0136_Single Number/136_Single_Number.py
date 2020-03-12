
from typing import List
# ハッシュマップ
def singleNumber(nums: List[int]) -> int:
    d = {}
    for num in nums:
        if num not in d: d[num] = 1
        else: d[num] += 1
    for key, value in d.items():
        if value == 1:
            return key

    # Time Complexity O(N)

#セットを使う方法
def singleNumber(num:List[int]) -> int:
    return 2 *(set(nums)) - sum(nums)


#ビット演算を使うと空間計算量が減る
def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res




print(singleNumber([1,2,3,2,3]))
