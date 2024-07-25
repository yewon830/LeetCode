from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1이 섬, 섬 갯수 찾기
        #bfs
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for _ in range(n)]
        def bfs(i,j):
            queue = deque([(i,j)])
            visited[i][j] = 1
            
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in [[-1,0],[1,0],[0,1],[0,-1]]:
                    nr = dr + cr
                    nc = dc + cc
                    if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        visited[nr][nc] = 1
            
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j)
                    cnt += 1
        return cnt
                    