/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    // 끝을 기준으로 오름차순 정렬, 아니라면 시작 중심으로 오름차순 정렬.
    // 배열 요소의 0번째 값을 기준으로, 내 앞에 있는 큰 값의 개수와 내 1번째 값을 비교한다. 
    // 내 앞에 있는 키 큰놈 개수가 나 1번째보다 많으면 나는 그 둘의 차이만큼 앞으로 간다.
    // 만약 적으면 그 둘의 차이만큼 뒤로간다.
    people.sort((a,b)=>{
        if(a[1]===b[1]){
            return a[0]-b[0]
        }
        return a[1]-b[1]
    })
    for(let i= 1;i<people.length;i++){
        let cnt = 0
        for(let j=0; j<i; j++){
            if(people[j][0] >= people[i][0]){
                cnt += 1
            }
        }
        if(cnt > people[i][1]){
            people.splice(i-(cnt-people[i][1]), 0, people[i])
            people.splice(i+1,1)
            
        }else if(cnt < people[i][1]){
            people.splice(i+(cnt-people[i][1]), 0 , people[i])
            people.splice(i,1)
            
        }

    }
    return people
    
};