"""
1041. Robot Bounded In Circle
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""
def isRobotBounded(instructions):
    dic = {1: [0, 1], 2: [1, 0], 3: [0, -1], 4: [-1, 0]}
    count = {"G": 0, "L": 0, "R": 0}
    start = [0,0]
    end = [0,0]
    key = 1
    def execute(instructions, end, key):
        for letter in instructions:
            count[letter] += 1
            if letter == "G":
                end[0] += dic[key][0]
                end[1] += dic[key][1]
            elif letter == "L":
                if key == 1:
                    key = 4
                else:
                    key -= 1   
            else:
                #letter R
                if key == 4:
                    key = 1
                else:
                    key += 1  
        return key
    trials = 0
    while trials < 5:
        key = execute(instructions, end, key)
        trials += 1
        if start == end:
            return True
    return False
        

instructions = "GGLLGG"
output = True
print(isRobotBounded(instructions), output)
instructions = "GG"
output = False
print(isRobotBounded(instructions), output)
instructions = "GL"
output = True
print(isRobotBounded(instructions), output)
instructions = "GLGLGGLGL"
output = False
print(isRobotBounded(instructions), output)
instructions = "LLGRL"
output = True
print(isRobotBounded(instructions), output)
instructions = "GRGRGGRR"
output = False
print(isRobotBounded(instructions), output)