'''
657. Robot Return to Origin
There is a robot starting at the position (0, 0), the origin,
on a 2D plane. 
Given a sequence of its moves, judge if this robot ends up 
at (0, 0) after it completes its moves.

You are given a string "moves" that represents the move
sequence of the robot where moves[i] represents its ith move.
Moves: 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it 
finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 
'R' will always make the robot move to the right once, 
'L' will always make it move left, etc. 
Also, assume that the magnitude of the robot's movement is
the same for each move.

1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.
'''
def judgeCircle2(moves):
    #To return there must be U paired with D, and L with R.
    moves_count = {"U": 0, "D": 0, "L": 0, "R": 0}
    for move in moves:
        moves_count[move] += 1
    return moves_count["U"] == moves_count["D"] and moves_count["L"] == moves_count["R"]

def judgeCircle(moves):
    UD_count = 0
    LR_count = 0
    for move in moves:
        if move == "U":
            UD_count += 1
        elif move == "D":
            UD_count -= 1
        elif move == "L":
            LR_count += 1
        else:
            LR_count -= 1
    return UD_count == 0 and LR_count == 0

#Tests
moves = "UD"
expected = True
print(judgeCircle(moves), judgeCircle(moves)==expected)

moves = "LL"
expected = False
print(judgeCircle(moves), judgeCircle(moves)==expected)

