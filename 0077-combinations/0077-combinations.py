class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backTracking(path,start):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(start,n+1):
                path.append(i)
                backTracking(path, i+1)
                path.pop()
        
        backTracking([],1)
        return result