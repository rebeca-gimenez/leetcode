'''
1232. Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], 
where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''
def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True
    #m = (y2 - y1) / (x2 - x1)
    point_1 = (coordinates[0][0], coordinates[0][1])
    point_2 = (coordinates[1][0], coordinates[1][1])
    if point_1[0] == point_2[0]:
        for point in coordinates[2:]:
            if not point[0] == point_1[0]:
                return False
    else:
        m = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0]) 
        for point in coordinates[2:]:
            if not int((point[0] - point_1[0]) * m) + point_1[1] == point[1]:
                return False
    return True
    
    
    
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
output = True
print(checkStraightLine(coordinates) == output)
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
output = False
print(checkStraightLine(coordinates) == output)
coordinates =
[[0,0],[0,1],[0,-1]]