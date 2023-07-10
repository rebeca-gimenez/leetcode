"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the 
elements on the secondary diagonal that are not part of the primary diagonal.

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""
def diagonalSum(mat):
    answer = 0
    for index in range(len(mat)):
        if index == len(mat) - 1 - index:
            answer += mat[index][index]
        else:
            answer += mat[index][index]
            answer += mat[index][len(mat) - 1 - index]
    return answer
            
mat = [[1,2,3], [4,5,6], [7,8,9]]
output = 25
print(diagonalSum(mat), output)
mat = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
output = 8
print(diagonalSum(mat), output)
mat = [[5]]
output = 5
print(diagonalSum(mat), output)