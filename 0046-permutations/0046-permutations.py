class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 순열
        result = []
        def backTracking(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
        
            for i in range(len(nums)):
                if(nums[i] not in path):
                    path.append(nums[i])
                    backTracking(path)
                    path.pop()
                
        backTracking([])
        return result
        