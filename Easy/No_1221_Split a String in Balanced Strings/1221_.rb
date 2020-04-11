#Runtime: 40 ms, faster than 17.00% of Ruby online submissions for Split a String in Balanced Strings.
#Memory Usage: 9.4 MB, less than 100.00% of Ruby online submissions for Split a String in Balanced Strings.

# 解法
# cntという変数をつくりrが出た時は１を引き、lが出た時は１を足す。
# cntがゼロの時は、一回ペアがあった（e.g. 'RRLL' or 'RL' or 'RRLRLL')
# cntの回数が答え

# @param {String} s
# @return {Integer}
def balanced_string_split(s)
    cnt = ans = 0
    s = s.split('')
    s.each do |c|
        if c == 'R'
            cnt += 1
        elsif c == 'L' then
            cnt -= 1
        end
        if cnt == 0
            ans += 1
        end
    end  
    return ans
end
