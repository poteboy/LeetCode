
//Runtime: 76 ms, faster than 58.30% of JavaScript online submissions for Add Digits.
//Memory Usage: 36.4 MB, less than 33.33% of JavaScript online submissions for Add Digits.

/**
 * @param {number} num
 * @return {number}
 */


var addDigits = function(num) {
    var result = 0
    var st = String(num)
    for (i = 0; i < st.length; i++){
        result += Number(st[i])
    }
    if (String(result).length >= 2){
        return addDigits(result);
    }else if (String(result).length === 1){
        return result;
    }
    
};
