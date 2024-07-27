class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #행 단위로 움직임
        # 행,열, 대각선 검사 필요
        board = [['.'] * n for _ in range(n)]
        result = []
        def check(r,c, board):
            if 'Q' in board[r]:
                return False
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
            #대각선 위로 검사
            i = r-1
            j = c-1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            k = r-1
            l = c+1
            while k>=0 and l<= n-1:
                if board[k][l] == 'Q':
                    return False
                k -= 1
                l += 1
            return True
        
        #백트래킹
        #행 단위, 지금 리스트라서 문자열로 조인 필요
        def backTracking(i, board):
            
            if i==n:
                result.append([''.join(row) for row in board])
                return
            
            for j in range(n):
                if check(i,j,board):
                    board[i][j] = 'Q'
                    backTracking(i+1,board)
                    board[i][j] = '.'
        backTracking(0,board)
        return result
                
            
            
                