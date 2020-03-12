class Solution:
    def reverse(self, x: int) -> int:
        if x ==0:
            return 0
        xlist = list(str(x))
        xlen = len(xlist)
        for i in range(xlen // 2):
            xlist[i], xlist[xlen - i -1] = xlist[xlen - i -1], xlist[i]
        if xlist[0] == '0':
            xlist.pop(0)
        if xlist[-1] == '-':
            xlist.pop(-1)
            xlist.insert(0, '-')
        reversedx = int(''.join(xlist))
        if reversedx > 2147483647 or reversedx < -2147483648:
            reversedx = 0
        return reversedx
        

