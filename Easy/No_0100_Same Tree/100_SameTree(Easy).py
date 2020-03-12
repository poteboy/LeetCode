
class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False
        if p.val != q.val:
            return False
        
        leftissame = self.isSameTree(p.left , q.left)
        rightissame = self.isSameTree(p.right, q.right)
        return leftissame and rightissame
