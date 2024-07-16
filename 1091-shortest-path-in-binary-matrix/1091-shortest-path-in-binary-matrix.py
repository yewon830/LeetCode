from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #가장 왼쪽에서 가장 오른쪽 모서리로 도착하는 가장 짧은 경로 수인듯?
        #8방향 대각선까지 이동 가능
        #0으로 이동, 밟은 노드 수 return
        # 만약 그리드 첫 시작이나 끝이 1이면 -1
        n =len(grid) #row,col n*n이라 동일함
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        visited = [[0]* n for _ in range(n)]
        queue = deque([(0,0,1)])
        visited[0][0] = 1
        while queue:
            cr, cc, cnt = queue.popleft()
            if cr == n-1 and cc == n-1:
                return cnt
            for dr,dc in [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]:
                nr = dr + cr
                nc = dc + cc
                #범위 내이고 그리드가 0이고 방문안했으면
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0 and not visited[nr][nc]:
                    queue.append((nr,nc, cnt+1))
                    #cnt도 넘겨주기.
                    visited[nr][nc] = 1
        return -1
                    
        
        