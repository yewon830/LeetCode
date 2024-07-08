import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 결과 모든걸 출력.
        #검증 로직 
        board = [['.']*n for _ in range(n)]
        result = []
        def check(board, r, c):
            if 'Q' in board[r]:
                return False
            for i in range(r):
                if board[i][c] == 'Q':
                    return False
            #왼쪽 대각선
            i = r - 1
            j = c -1
            while(i>=0 and j>=0):
                if(board[i][j]== 'Q'):
                    return False
                i -= 1
                j -= 1
            # 오른쪽 대각선
            k = r -1
            l = c + 1
            while (k>=0 and l<=n-1):
                if(board[k][l] == 'Q'):
                    return False
                k -= 1
                l += 1
                
            return True
        
        def backTracking(board, i):
            
            if i == n:
                result.append([''.join(row) for row in board])
                return
            #행 단위로 옮기기
            for j in range(n):
                if(check(board,i,j)):
                    board[i][j] = 'Q'
                    backTracking(board, i+1)
                    board[i][j] = '.'
        backTracking(board, 0)
        return result
            