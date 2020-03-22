//Runtime: 64 ms, faster than 63.64% of JavaScript online submissions for Missing Number.
//Memory Usage: 35.8 MB, less than 97.14% of JavaScript online submissions for Missing Number.


/**
 * @param {number[]} nums
 * @return {number}
 */

const arrSum = nums => nums.reduce((a,b) => a + b, 0)

var missingNumber = function(nums) {
    const arrSum = nums => nums.reduce((a,b) => a + b, 0);

    return  (nums.length * (nums.length +1) / 2) - arrSum(nums);
};
