
//Runtime: 4 ms, faster than 94.65% of Go online submissions for Two Sum II - Input array is sorted.
//Memory Usage: 3.1 MB, less than 25.00% of Go online submissions for Two Sum II - Input array is sorted.


func twoSum(numbers []int, target int) []int {
    ans := make(map[int]int)
    
    for k,v := range numbers {
        _,ok := ans[v]
        if ok ==true {
            return []int{ans[v] + 1, k +1}
        } else {
            ans[target - v] = k
        }
    }
    return []int{0,0}
}
