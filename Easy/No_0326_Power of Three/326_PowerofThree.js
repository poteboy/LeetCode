// JavaScript２問目。pythonでやった時とほぼ同じことをしているが、run timeがこっちの方が92％ほど高い。

//Runtime: 188 ms, faster than 97.45% of JavaScript online submissions for Power of Three.
//Memory Usage: 48.1 MB, less than 30.00% of JavaScript online submissions for Power of Three.

/**
 * @param {number} n
 * @return {boolean}
 */
var n = 3;

var isPowerOfThree = function(num) {
    if (num === 1){
        return true;
    }else{
        return power(n, num);
    }
    
};

function power(n, num){
    if (n == num){
        return true;
    }else if(n < num){
        n *= 3;
        return power(n, num);
    }else{
        return false;
    }
};


