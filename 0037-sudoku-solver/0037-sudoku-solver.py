class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 스도쿠 풀기
        # 1; 행,열, 3*3 검증
        # 2. 한칸씩 이동, 백트래킹 돌려서 하나씩 검증하기
        
        def check(r,c,n):
            # 행 검사
            if n in board[r]:
                return False
            for i in range(9):
                if n == board[i][c]:
                    return False
            start_r, start_c = (r//3)*3, (c//3)*3
            for i in range(start_r, start_r+3):
                for j in range(start_c, start_c+3):
                    if board[i][j] == n:
                        return False
            return True
        
        #백트래킹
        def backTracking(index):
            if index == 81:
                return True
            
            i, j = index//9, index%9
            
            if board[i][j] == ".":
                for n in map(str, range(1,10)):
                    # 수 하나씩 넣어보기
                    if check(i,j,n):
                        board[i][j] = n
                        if backTracking(index+1):
                            return True
                        board[i][j] = "."
                return False
            else:
                return backTracking(index+1)
        
        backTracking(0)
                
            
        
        