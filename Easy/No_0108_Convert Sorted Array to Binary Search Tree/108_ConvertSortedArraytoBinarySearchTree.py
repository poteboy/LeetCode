


#二分探索と再帰の応用

#解説なしでは解けなかったので要復習

#Runtime: 68 ms, faster than 90.85% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
#Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        pl = 0
        pr = len(nums) -1 

        def convertBST(pl,pr):
            if pl > pr: #右が左を超えるときはそこにノードが入らない
                return None 
            mid = (pl + pr) // 2
            Node = TreeNode(nums[mid])
            if pl == pr: #右と左が同じの時はそのNode以降に何も続かない
                return Node
            Node.left = convertBST(pl, mid -1) #同じ作業を真ん中のNode（根）以降も続ける（左木）
            Node.right = convertBST(mid +1, pr) #同じ作業を真ん中のNode（根）以降も続ける（右木）
            return Node
        return convertBST(pl, pr)
