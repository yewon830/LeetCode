class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board) # 세로
        m = len(board[0]) # 가로
        visited = [[0]*m for _ in range(n)] # 방문 여부
        
        def backTracking(cr,cc,w, visited):
            #. 방문 안했고 글자가 같으면
            if not visited[cr][cc] and board[cr][cc] == word[w]:
                if w ==len(word)-1:
                    return True #찾았다
                visited[cr][cc] = 1
                flag = False
                
                for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    # 이동 했을 때 범위 내인가?
                    if 0<=dr+cr<n and 0<=dc+cc<m:
                        nr = dr + cr
                        nc = dc + cc
                        # 백트래킹 해서 잘 되고 있으면
                        if backTracking(nr,nc,w+1, visited):
                            flag = True

                visited[cr][cc] = 0
                return flag
        
        for i in range(n):
            for j in range(m):
                if backTracking(i, j, 0, visited):
                    return True

        return False
                    
            
            
               
        
