
#Runtime: 64 ms, faster than 46.86% of Ruby online submissions for Palindrome Number.
#Memory Usage: 9.3 MB, less than 100.00% of Ruby online submissions for Palindrome Number.


# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    if x < 0
        return false
    end
    x = x.to_s
    if x.size ==1
        return true
    end
    num = x.size / 2

    for i in 1..num do
        if x[i-1] != x[-i]
            return false 
        end 
    end
    return true
end
