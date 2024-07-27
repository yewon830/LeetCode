class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 행 단위로 움직이기 #나중에 문자열로 쪼인 해야함
        result = []
        board = [['.']*n for _ in range(n)]
        def check(board,r,c):
            if 'Q' in board[r]:
                return False
            for i in range(r):
                if board[i][c] == 'Q':
                    return False
            #대각선 검사(내 위쪽으로)
            i = r-1
            j = c-1
            #왼쪽 대각선
            while i>= 0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1 
            k = r-1
            l = c +1
            while k >= 0 and l <= n-1:
                if board[k][l] == 'Q':
                    return False
                k -= 1
                l += 1

            return True
        
        def backTracking(i, board):
            if i == n:
                result.append([''.join(row) for row in board])
                return
            
            for j in range(n):
                if check(board,i,j):
                    board[i][j] = 'Q'
                    backTracking(i+1,board)
                    board[i][j] = '.'
        backTracking(0,board)
        return result
            
            
