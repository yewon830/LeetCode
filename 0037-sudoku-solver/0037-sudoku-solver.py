class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 모든 경우의 수를 탐색하되, 지금 기준으로 행-열-칸을 검사해서 없는 수만 넣는다.
        # 만약에 수를 더 넣을 수 없거나, 백트래킹을 종료해야 하면 '.'으로 원상복구한다. 
        # 한 row의 마지막 인덱스에 j가 도달했다면, i +1
        def check(i,j,num):
            flag = True
            # 행 검사 : board[i]에 숫자가 겹치는게 있는지
            if(num in board[i]):
                flag = False
            # 열 검사 : for문 돌려서 board[i][지금] 번에 숫자가 겹치는 게 있는지
            for k in range(9):
                if(num in board[k][j]):
                    flag = False
            # 칸 검사 : 시작점 알아내서 3칸씩
            start_i = (i//3)*3
            start_j = (j//3)*3
            for k in range(start_i, start_i+3):
                for l in range(start_j, start_j+3):
                    if(board[k][l]==num):
                        flag = False
            return flag

        # 백트래킹
        def backTracking(i,j):
            if i == 9:
                return True
            elif j == 9 :
                return backTracking(i + 1, 0)
            if board[i][j] == '.':
                #범위 내라면
                for num in ['1','2','3','4','5','6','7','8','9']:
                    if check(i,j,num):
                        board[i][j] = num
                        if backTracking(i,j+1):
                            return True
                        board[i][j] = '.'
                return False
            else:
                return backTracking(i, j+1)
           
        backTracking(0,0)
        