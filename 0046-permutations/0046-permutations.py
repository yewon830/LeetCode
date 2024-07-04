class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backTracking(perm):
            
            if len(perm) == len(nums):
                result.append(perm[:])
                return 
            
            for i in range(len(nums)):
                if(nums[i] not in perm):
                    perm.append(nums[i])
                    backTracking(perm)
                    perm.pop()
                
        backTracking([])
        return result