class Solution:
    def climbStairs(self, n: int) -> int:
        # 1,2칸을 +하며 n에 도달할 수 있는 방법의 가짓수 구하기
        # 점화식: n에 도달하는 방법은 1칸전에 도달하는 경우의 수 + 2칸전에 도달하는 경우의 수
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
