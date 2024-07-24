from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n= len(grid)
        #0,0에서 시작해서 n-1,n-1로 끝남
        # 만약 첫 시작이나 끝이 1이라면 그냥 -1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        queue = deque()
        queue.append((0,0,1))

        visited = [[0]*n for _ in range(n)]
        
        while queue:
            cr,cc, cnt = queue.popleft()
            if cr == n-1 and cc == n-1:
                return cnt
            #8방향 이동
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,-1],[1,1],[-1,1]]:
                nr = dr + cr
                nc = dc + cc
                if 0<= nr< n and 0<= nc<n and grid[nr][nc] == 0 and not visited[nr][nc]:
                    queue.append((nr,nc,cnt+1))
                    visited[nr][nc] = 1
        return -1
                     
        