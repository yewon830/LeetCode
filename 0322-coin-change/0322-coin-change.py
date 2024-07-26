from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #코인을 누적으로 더해준다
        #queue에 지금 합, cnt를 넣는다.
        # 총량을 찾으면 .cnt 반환한다
        # 총량보다 적을 때만 append한다
        if amount == 0:
            return 0
        
        queue = deque([(0,0)])
        visited = set()
        while queue:
            money, cnt = queue.popleft()
            if money == amount:
                return cnt
            for i in range(len(coins)):
                next_money = coins[i] + money
                if next_money not in visited and next_money <= amount:
                    queue.append((next_money, cnt+1))
                    visited.add(next_money)
        return -1
            
        
                    
        
        
        
        