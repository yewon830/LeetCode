import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 결과 모든걸 출력.
        #검증 로직 
        board = [['.']*n for _ in range(n)]
        result = []
        
        def check(r,c):
            if 'Q' in board[r]:
                return False
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
            for x,y in [[-1,-1],[1,1],[-1,1],[1,-1]]: #대각선 검사
                for jump in range(1,n+1):
                    if 0<=r+(x*jump)<n and 0<=c+(y*jump)<n:
                        if 'Q' == board[r+(x*jump)][c+(y*jump)]:
                            return False
            return True

        def backTracking(c,path):
            cnt = 0;
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'Q':
                        cnt += 1
            if cnt == n:
                new_path = copy.deepcopy(path)
                result.append(''.join(row) for row in new_path)
                return True
            
            for i in range(n):
                if check(i, c):
                    path[i][c] = 'Q'
                    backTracking(c + 1,path)
                    path[i][c] = '.'
        
        backTracking(0,board)
        return result
            