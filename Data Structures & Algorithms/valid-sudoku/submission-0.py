class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    if ((i,num) in visited 
                    or (num, j) in visited
                    or (i//3,j//3,num) in visited):
                        return False
                    
                    visited.add((i,num))
                    visited.add((num, j))
                    visited.add((i//3,j//3,num))
        return True
