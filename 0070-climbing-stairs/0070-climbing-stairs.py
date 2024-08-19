class Solution:
    def climbStairs(self, n: int) -> int:
        # 1,2로 n에 도달할 수 있는 방법의 가짓수 구하기
        dp = [0]*(n+1)
        #초기세팅
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        