class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backTracking(start,path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start,n+1):
                path.append(i)
                backTracking(i+1,path)
                path.pop()
        backTracking(1,[])
        return result