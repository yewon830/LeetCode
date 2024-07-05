class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #순열의 경우 1,2,3 1,3,2 가 다르다. 이전인덱스도 볼 수 있다.
        result = []
        def backTracking(path):
            # 베이스 케이스 : n개 다 채우면 끝
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for e in nums:
                if(e not in path):
                    path.append(e)
                    backTracking(path)
                    path.pop()
                                
            
        backTracking([])
        return result