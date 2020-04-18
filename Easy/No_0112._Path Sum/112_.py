
#Runtime: 40 ms, faster than 80.61% of Python3 online submissions for Path Sum.
#Memory Usage: 15.6 MB, less than 5.45% of Python3 online submissions for Path Sum.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None

n5 = TreeNode(5)
n4 = TreeNode(4)
n8 = TreeNode(8)
n5.left = n4
n5.right = n8
n11 = TreeNode(11)
n4.left = n11
n7 = TreeNode(7)
n2 = TreeNode(2)
n11.left = n7
n11.right = n2


def PathSum(root: TreeNode, x: int):
    #もしノードが無ければ、その時点で正解はないからFalse
    if root is None:
        return False
        
    #ノードがあったらｍその値でsumを引く
    x-= root.val
    
    #それ以上子がいなく、sumが０なら答え
    if not root.left and not root.right and x == 0:
        return True
    
    return PathSum(root.left, x) or PathSum(root.right, x)


print(PathSum(n5, 22))
