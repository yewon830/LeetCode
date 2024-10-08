class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]* len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2,len(nums)):
            # 내 앞 인덱스 제외하고 내 이전 중에서 제일 큰 값과 더한다
            max_cnt = 0
            for j in range(i-1):
                if max_cnt < dp[j]:
                    max_cnt = dp[j]
            dp[i] = nums[i] + max_cnt
        
        return max(dp)