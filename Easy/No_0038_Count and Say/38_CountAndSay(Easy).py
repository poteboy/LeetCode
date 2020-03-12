
class Solution:
    def countAndSay(self, n: int) -> str:
        final = '1'
        if n == 1:
            return final
        for _ in range(n-1):
            final = self.next_str(final)
        return ''.join(final)

    def next_str(self, seq:str):
        ans = []
        target = seq[0]
        count = 0
        i = 0
        while True:
            if i > len(seq) -1:
                break
            if seq[i] == target:
                count += 1
                i += 1
            else:
                ans += str(count)
                ans += target
                target = seq[i]
                count = 0
        ans += str(count)
        ans += target
        return ans


