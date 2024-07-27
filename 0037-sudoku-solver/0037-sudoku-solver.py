class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #1칸씩 움직이면서 모든 경우의 수 탐색하기
        # .이면 움직이고,
        # visited = [[0]*9 for _ in range(9)]
        def check(r,c,num):
            # 행 검사(같은 수 없어야)
            if num in board[r]:
                return False
            for i in range(9):
                    if board[i][c] == num:
                        return False
            s_row = (r//3)*3
            s_col = (c//3)*3
            for i in range(s_row, s_row+3):
                for j in range(s_col, s_col+3):
                    if board[i][j] == num:
                        return False
            return True
        
        def backTracking(idx):
            if idx == 81:
                return True
            r = idx//9
            c = idx % 9
            if  board[r][c]== '.' :
                for i in map(str,range(1,10)):
                    if check(r,c,i):
                        board[r][c] = i
                        if backTracking(idx+1):
                            return True
                        board[r][c] = '.'
            else:
                return backTracking(idx+1)
        backTracking(0)
