//Runtime: 56 ms, faster than 50.23% of JavaScript online submissions for Pascal's Triangle II.
//Memory Usage: 33.9 MB, less than 50.00% of JavaScript online submissions for Pascal's Triangle II.


/**
  * 解法
  *　空の配列にまず1を追加する。そしてその下のforループの全ての処理が終わった後に1を追加する。（1で始まり1で終わる）
  *  そのループの条件はi <= rowIndex（受け取った値）なので、もし受け取った値が１なら[1]を返す。
  *   その下のもう一つのforループで1に挟まれた中身の部分をつくっていく。
  *  配列のindexの時の値は、前の列の同じindex + 前の列の同じindex - 1なので、この２個目のforループでは新しい配列をつくる
  */　１個目のforループは新しい配列をつくる回数。

/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex){
    let row = [];
    if (rowIndex < 0){
        return row;
    }
    row.push(1);
    
    for (let i = 1; i <= rowIndex; i++){
        for (let j = row.length -1; j > 0; j--){
            row[j] = row[j -1] + row[j];
        }
        row.push(1);
    }
    return row
}
