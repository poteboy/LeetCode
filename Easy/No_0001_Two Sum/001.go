//Runtime: 8 ms, faster than 39.56% of Go online submissions for Two Sum.
//Memory Usage: 4 MB, less than 7.69% of Go online submissions for Two Sum.


func twoSum(nums []int, target int) []int {
    
    hash := make(map[int]int)
    for i, v := range nums {
        _, ok := hash[v]
        if ok == true{
            return []int{hash[v], i}
        } else{
            hash[target - v] = i
        }
    }
    return []int{0,0}
}

// 最後のreturn文は恐らく決まりみたいなもの？
// 使いたくない変数は_にする。（ohterwise it will throw error）
