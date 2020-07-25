
# Runtime: 60 ms, faster than 47.28% of Ruby online submissions for Two Sum.
# Memory Usage: 10.2 MB, less than 6.83% of Ruby online submissions for Two Sum.

def two_sum(nums, target)
    hash = {}
    
    nums.each_with_index do |n, i|
        if hash[target - n] != nil
            return hash[target - n], i
        end
        hash[n] = i
    end
end
