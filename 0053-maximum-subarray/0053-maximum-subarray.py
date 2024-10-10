class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 합계가 가장 큰 sub 배열 찾기
        # 완탐은 안될거같음 배열 너무 김.
        # dp[i]에는 지금까지의 인덱스에서 만들 수 있는 sub 배열의 최대 합이 들어간다. 
        #   만약에 dp의 이전 값이 음수라면 포함시키지 않는다.(손해)
        #   만약에 양수면은 포함시킨다.
        #   dp의 max값을 return한다
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            
        return max(dp)
        