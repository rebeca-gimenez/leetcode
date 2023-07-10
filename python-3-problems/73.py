'''
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's.
You must do it in place.

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''
def setZeroes(matrix):
    row_zeroes = set()
    col_zeroes = set()
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 0:
                row_zeroes.add(row_idx)
                col_zeroes.add(col_idx)
    for row in row_zeroes:
        matrix[row] = [0]*len(matrix[0])
    for col in col_zeroes:
        for row_idx in range(len(matrix)):
            matrix[row_idx][col] = 0
                
                
            
            
matrix = [[1,1,1],[1,0,1],[1,1,1]]
output = [[1,0,1],[0,0,0],[1,0,1]]
setZeroes(matrix)
print(matrix==output)
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
setZeroes(matrix)
print(matrix==output)