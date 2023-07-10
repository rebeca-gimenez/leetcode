'''
1351. Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing 
order both row-wise and column-wise, return the number of 
negative numbers in grid.

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

Could you find an O(n + m) solution?
'''

def countNegatives(grid):
    def binary_search(row, left, right):
        if left > right:
            return -1
        else:
            middle = int((left + right)/2)
            if row[middle] < 0:
                if middle - 1 >= 0 and row[middle - 1] < 0:
                    return binary_search(row, left, middle - 1)
                else:
                    return middle
            else:
                return binary_search(row, middle + 1, right)
    count = 0
    for row in grid:
        if row[0] < 0:
            count += len(row)
        elif row[-1] >= 0:
            count += 0
        else:
            count += len(row) - binary_search(row, 0, len(row) - 1)
    return count
 
grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]
output = 8
print(countNegatives(grid))
grid = [[3,2],
        [1,0]]
output = 0
print(countNegatives(grid))