class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 단어 인덱스를 늘려가면서 하나씩 비교
        n = len(board)
        m = len(board[0])
        visited = [[0]*m for _ in range(n)]
        def backTracking(r,c,w):
            if board[r][c] == word[w] and not visited[r][c]:
                visited[r][c] = 1
                if w == len(word)-1:
                    return True
            
                for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<n and 0<=nc<m :
                        if backTracking(nr,nc,w+1):
                            return True
                visited[r][c] = 0
       
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and not visited[i][j]:
                    if backTracking(i,j,0):
                        return True
        return False
        
        

            
        
        
        