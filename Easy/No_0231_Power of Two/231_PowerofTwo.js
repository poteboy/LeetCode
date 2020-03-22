//Runtime: 72 ms, faster than 71.99% of JavaScript online submissions for Power of Two.
//Memory Usage: 35.6 MB, less than 38.46% of JavaScript online submissions for Power of Two.


/**
 * @param {number} n
 * @return {boolean}
 */

var num = 2

var isPowerOfTwo = function(n) {
    if (n === 1){
        return true;
    }else{
        return check(n, num);
    }
    
};

const check = function(n, num){
    if (n === num){
        return true;
    }else if (n > num){
        num = num * 2;
        return check(n,num);
    }else if (num > n){
        return false;
    }
}
