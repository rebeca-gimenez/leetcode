"""
1337. The K Weakest Rows in a Matrix
You are given an m x n binary matrix mat of 1's (representing soldiers) 
and 0's (representing civilians). 
The soldiers are positioned in front of the civilians. 
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""
def kWeakestRows(mat, k):
    soldiers = []
    index = 0
    for row in mat:
        soldiers.append((sum(row), index))
        index += 1
    soldiers.sort()
    answer = []
    for soldier in soldiers:
        answer.append(soldier[1])
    return answer[:k]
mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
k = 3
output = [2,0,3]
print(kWeakestRows(mat, k))
mat = [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]]
k = 2
output = [0,2]
print(kWeakestRows(mat, k))