/**
 * @param {string} s
 * @return {boolean}
 */
var stack = [];
var isValid = function(s){
    if (s.length % 2 !== 0){
        return false;
    }
    for (i = 0; i < s.length; i++){
        if(s[i] === '(' || s[i] === '{' || s[i] === '['){
            stack.push(s[i]);
        }else if (s[i] === ')' && stack.length !== 0 && stack[stack.length -1] === '('){
            stack.pop();
        }else if (s[i] === '}' && stack.length !== 0 && stack[stack.length -1] === '{'){
            stack.pop();
        }else if (s[i] === ']' && stack.length !== 0 && stack[stack.length -1] === '['){
            stack.pop();
        }
    }
    if (stack.length === 0){
        return true;
    }else{
        return false;
    }

}
