class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 부분 집합은 중복은 허용 x 인데 중간 과정을 포함해야 한다.
        result = []
        def backTracking(start,path):
            
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backTracking(i+1, path)
                path.pop()
        backTracking(0,[])
        return result
                