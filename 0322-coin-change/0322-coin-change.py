from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #코인을... 누적으로 더해주면서 cnt 출력
        if amount == 0:
            return 0
        
        queue = deque([(0,0)])
        visited = set()
        
        while queue:
            cur_coin, cnt = queue.popleft()
            if cur_coin == amount:
                return cnt
            for i in range(len(coins)):
                next_coin = cur_coin + coins[i]
                if next_coin not in visited and next_coin<= amount:
                    queue.append((next_coin,cnt+1))
                    visited.add(next_coin)
        return -1
        
                    
        
        
        
        