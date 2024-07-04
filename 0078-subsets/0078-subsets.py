class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backTracking(start, subsetList):
            
            result.append(subsetList[:])
            
            
            for i in range(start, len(nums)):
                subsetList.append(nums[i])
                backTracking(i+1, subsetList)
                subsetList.pop()
        backTracking(0, [])
        return result
