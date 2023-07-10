"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
def spiralOrder(matrix):
    lenght = int(len(matrix)*len(matrix[0]))
    spiral = []
    cur_row = 0
    cur_col = 0
    step = 1
    while len(spiral) < lenght:
        if step == 1:
            col_range = range(0, len(matrix[0]),step)
        else:
            col_range = range(len(matrix[0]) - 1, -1,step)
        for col in col_range:
            #print((cur_row, col))
            spiral.append(matrix[cur_row][col])
            cur_col = col
        try:
            matrix.pop(cur_row)
        except:
            print("Error pop cur_row")
        if step == 1:
            row_range = range(0, len(matrix),step)
        else:
            row_range = range(len(matrix) - 1, -1,step)
        #print(matrix)
        for row in row_range:
            #print((row,cur_col))
            spiral.append(matrix[row][cur_col])
            try: 
                matrix[row].pop(cur_col)
            except:
                print("Error")
            cur_row = row
        #print("end of loop")
        #print(matrix)
        step = step*(-1)
    return spiral

    
matrix =  [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
print(spiralOrder(matrix))
matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = [1,2,3,6,9,8,7,4,5]
print(spiralOrder(matrix)==output)
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
output = [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiralOrder(matrix)==output)
