from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 0만 이동
        # 8방향 이동 n * n
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = deque([(0,0,1)])
        visited = [[0]*n for _ in range(n)]
        visited[0][0] = 1
        
        while queue:
            cr,cc,cnt = queue.popleft()
            if cr == n-1 and cc == n-1:
                #도착
                return cnt
            for dr,dc in [[-1,0],[1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]:
                nr = dr + cr
                nc = dc + cc
                # 범위 내, 노중복, 0
                if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc] == 0:
                    queue.append((nr,nc,cnt+1))
                    visited[nr][nc] = 1
        return -1
                     
        