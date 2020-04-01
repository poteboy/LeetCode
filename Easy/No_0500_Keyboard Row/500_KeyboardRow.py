#３通り解法を思いついたが、中でも一番遅そうな一番最初のコードが一番はやい。メモリはどれも同じだけ使用してる。

class Solution:
    def __init__(self):
        self.first = ['q','w','e','r','t', 'y', 'u', 'i','o','p']
        self.mid = ['a', 's', 'd', 'f','g','h', 'j', 'k', 'l']
        self.last = ['z', 'x', 'c','v', 'b', 'n', 'm']
        self.ans = []
        
    def findWords2(self, words):
        #Runtime: 28 ms, faster than 60.71% of Python3 online submissions for Keyboard Row.
        #Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Keyboard Row.
        for w in words:
            word = w.lower()
            i = 0
            while True:
                if i == len(word):
                    self.ans.append(w)
                    i = 0
                    break
                if word[i] in self.first:
                    i += 1
                else:
                    i = 0
                    break
            while True:
                if i == len(word):
                    self.ans.append(w)
                    i = 0
                    break
                if word[i] in self.mid:
                    i += 1
                else:
                    i = 0
                    break
            while True:
                if i == len(word):
                    self.ans.append(w)
                    i = 0
                    break
                if word[i] in self.last:
                    i += 1
                else:
                    i = 0
                    break
        return self.ans

    def findWords(self, words):
        # A <= B で左辺の要素が全て右辺に含まれているか判定
        #Runtime: 32 ms, faster than 14.63% of Python3 online submissions for Keyboard Row.
        #Memory Usage: 13.6 MB, less than 6.67% of Python3 online submissions for Keyboard Row.
        for w in words:
            word = w.lower()
            if set(word) <= set(self.first):
                self.ans.append(w)
            elif set(word) <= set(self.mid):
                self.ans.append(w)
            elif set(word) <= set(self.last):
                self.ans.append(w)
            else:
                pass
        return self.ans
    
    def findWords(self, words):
        #Runtime: 32 ms, faster than 14.63% of Python3 online submissions for Keyboard Row.
        #Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Keyboard Row.
        return [ w for w in words if set(w.lower()).issubset(self.mid)or\
                set(w.lower()).issubset(self.first) or set(w.lower()).issubset(self.last)\
               ]
    # num <= nums と num.issubset(nums) は同じ意味

            
