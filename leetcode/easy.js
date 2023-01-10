/**
 * @param {string} s
 * @return {number}
 */

var romanToInt = function(s){
    var roman_int= {"I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000
                    };
    var control_sum = 0;
    for (let i = 0; i < s.length; i++){
        if(i + 1 < s.length && roman_int[s[i]] < roman_int[s[i + 1]]){
            control_sum -= roman_int[s[i]];
        }
        else{
            control_sum += roman_int[s[i]];
        }
    };

    return(control_sum);
};

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let mini = Math.min.apply(null,strs.map((e) => e.length));
    let prefix = "";
    for (let i = 0; i < mini; i++){
        let correct_for_prefix = true
        for (let s = 1; s < strs.length; s++){
            if(strs[s - 1][i] != strs[s][i]){ correct_for_prefix = 0 };
       };
       if (correct_for_prefix){ prefix += strs[0][i] } else { break; }
    };
    return prefix;
};

console.log(longestCommonPrefix(["dog","racecar","car"]))
console.log(longestCommonPrefix(["flower","flow","flight"]))