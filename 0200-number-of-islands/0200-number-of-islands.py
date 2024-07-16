from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #사방으로 이동
        #연결되어있으면 섬 col이 n 이고 row가 m
        n = len(grid[0]) #col
        m = len(grid) #row
        cnt = 0;
        visited = [[0]*n for _ in range(m)]
        #여러 곳에서 시작해야. 
        
        def bfs(i,j):
            queue = deque()
            queue.append([i,j])
            visited[i][j] = 1
            while queue:
                cr, cc = queue.popleft()
                #수평 수직이동이므로 동서남북
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr = cr + dr
                    nc = cc + dc
                    #범위 검사 + 방문x + 그리드에서 섬이면
                    if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc] == "1":
                        queue.append([nr,nc])
                        visited[nr][nc] = 1
        
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=="1":
                    bfs(i,j)
                    cnt += 1
        return cnt
        