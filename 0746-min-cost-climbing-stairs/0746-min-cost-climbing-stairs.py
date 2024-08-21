class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 비용을 지불하면 한계단 or 두계단을 오를 수 있다.
        
        #인덱스가 0이나 1에서 시작할 수 있다.
        #꼭대기 도달 최소비용. 
        # dp테이블에 지금까지 드는 최소비용.
        
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]