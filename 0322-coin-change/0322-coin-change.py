from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bfs말고 dp로 풀어보자
        dp = [1000000]*(amount+1) #여기에 idx가 coin으로 도달할 수 있는 최소 갯수 들어있음
        
        dp[0]=0
        for i in range(amount+1):
            #하나씩 더하기(코인이 몇개인지 모름)
            for coin in coins:
                # 지금 idx + coin이 zmount보다 작으면
                if i+coin <=amount:
                    dp[i+coin]=min(dp[i]+1, dp[i+coin]) #코인 더하기 전+1,
        
        if dp[amount] == 1000000:
            return -1
        return dp[amount]
            
        
                    
        
        
        
        