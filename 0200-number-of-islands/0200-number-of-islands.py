from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        #1이 섬
        visited = [[0] *m for _ in range(n)]
        def bfs(i,j):
            queue = deque([(i,j)])
            visited[i][j] = 1
            while queue:
                ci, cj = queue.popleft()
                for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    ni = dr + ci
                    nj = dc + cj
                    if 0<=ni<n and 0<=nj<m and grid[ni][nj] =="1" and not visited[ni][nj]:
                        queue.append((ni,nj))
                        visited[ni][nj] = 1        
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j)
                    cnt += 1
                    
        return cnt
        