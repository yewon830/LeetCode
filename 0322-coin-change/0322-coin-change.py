from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # 이거 중복 가능..[1,2,5] 각각이  [1,2,5] 로 갈 수 있음.
        # cnt 넘겨주기
        queue = deque([(0,0)]) #현재금액, cnt
        visited = set()

        while queue:
            cur_coin, cnt = queue.popleft()
            if cur_coin == amount:
                return cnt
            for i in range(len(coins)):
                next_coin = cur_coin + coins[i]
                if next_coin not in visited and next_coin <= amount:
                    queue.append((next_coin, cnt+1))
                    visited.add(next_coin)
        return -1
                    
        
        
        
        