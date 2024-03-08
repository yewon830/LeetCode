/**
 * @param {number[]} prices
 * @return {number}
 */
 // 거래를 여러번 할 수 있는데, 이떄 최대 이익. 
 //이거 두 쌍 짓는거랑 비슷하지 않나?
 // 여러 번 팔 수 있으니까, 여러 번 거래를 하면 됨
 // 내 뒷번에 있는 수가 나보다 크면 내 뒷번 - 나
var maxProfit = function(prices) {
    let res = 0
    for(let i=0; i<prices.length-1; i++){
        if(prices[i] < prices[i+1]){
            res += prices[i+1] - prices[i]
        }
    }
    return res
};