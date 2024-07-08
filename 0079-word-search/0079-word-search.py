class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 상하 좌우로 돌면서, 단어가 만들어지는지 백트래킹으로 체크
        #  종료 조건 = [w가 마지막 인덱스 도달
        # visited 활용해서 방문 요소 체크
        n = len(board)
        m = len(board[0])
        visited = [[0] * m for _ in range(n)]
        
        def backTracking(i,j,w):
            
            if not visited[i][j] and board[i][j] == word[w]:
                visited[i][j] = 1
                if w == len(word)-1:
                    return True
                
                for x,y in [[-1,0],[1,0],[0,1],[0,-1]]:
                    if 0<=i+x<n and 0<= j+y<m: #범위 검사
                        if backTracking(i+x, j+y, w+1):
                            return True
                visited[i][j] = 0
            
            return False
        
        for i in range(n):
            for j in range(m):
                if backTracking(i,j,0):
                    return True
        return False
                
                            
        
        
            

            
                    
            
            
               
        
