
#Runtime: 64 ms, faster than 24.73% of Python3 online submissions for Find Mode in Binary Search Tree.
#Memory Usage: 18.4 MB, less than 8.33% of Python3 online submissions for Find Mode in Binary Search Tree.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 
from typing import Dict, List

from collections import Counter
class Solution(object):
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        tmp = []
        def preorder(root, tmp):
            if root:
                preorder(root.left , tmp)
                preorder(root.right, tmp)
                tmp.append(root.val)
        preorder(root, tmp)
        cnt = Counter(tmp)
        print(cnt)
        max_cnt = cnt.most_common()[0][1]
        return [k for k,v in cnt.items() if v == max_cnt]

node1 = TreeNode(1)
node2 = TreeNode(2)
node1.right = node2
node3 = TreeNode(2)
node2.left = node3
node4 = TreeNode(1)
node3.right = node4

s = Solution
print(s.findMode(node1))
#print(solution(node1))
