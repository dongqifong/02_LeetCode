from os import system
system('clear')
'''
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''
class Solution:
    def isValidSudoku(self, board) -> bool:
        #check row
        for i in range(9):
            seen_row={}
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen_row:
                    return False
                else:
                    seen_row[board[i][j]]=True
        #check col   
        for j in range(9):
            seen_col={}
            for i in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen_col:
                    return False
                else:
                    seen_col[board[i][j]]=True
        
        row=[1,4,7]
        col=[1,4,7]
        for center_r in row:
            for center_c in col:
                seen_matrix={}
                for k in [-1,0,1]:
                    for j in [-1,0,1]:
                        if board[center_r+k][center_c+j]=='.':
                            continue
                        if board[center_r+k][center_c+j] in seen_matrix:
                            return False
                        else:
                            seen_matrix[board[center_r+k][center_c+j]]=True
        return True