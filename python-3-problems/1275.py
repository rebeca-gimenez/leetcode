'''
1275. Find Winner on a Tic Tac Toe Game
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Rules:
1. Players take turns placing characters into empty squares ' '.
2. The first player A always places 'X' characters,
while the second player B always places 'O' characters.
3. 'X' and 'O' characters are always placed into empty 
squares, never on filled ones.
4. The game ends when there are three of the same (non-empty)
 character filling any row, column, or diagonal.
5. The game also ends if all squares are non-empty.
6. No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid 
(i.e., it follows the rules of Tic-Tac-Toe), 
the grid is initially empty, and A will play first.

1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
'''
def tictactoe(moves):
    board = [["" for dummy_col in range(3)] for dummy_row in range(3)]
    player = "X"
    for coord in moves:
        board[coord[0]][coord[1]] = player
        player = switch_player(player)
    return check_win(board)

def switch_player(player):
    if player == "X":
        return "O"
    if player == "O":
        return "X"
    
def check_win2(board):
    #In a nxn board, there are n rows, n columns, 2 diagonals
    diag1_count = {"X": 0, "O": 0, "": 0}
    diag2_count = {"X": 0, "O": 0, "": 0}
    global_count = {"X": 0, "O": 0, "": 0}
    for index1 in range(len(board)):
        diag1_count[board[index1][index1]] += 1
        diag2_count[board[index1][len(board) - 1 - index1]] += 1
        row_count = {"X": 0, "O": 0, "": 0}
        col_count = {"X": 0, "O": 0, "": 0}
        for index2 in range(len(board)):
            row_count[board[index1][index2]] += 1
            col_count[board[index2][index1]] += 1
            global_count[board[index2][index1]] += 1
        if 3 in row_count.values() or 3 in col_count.values():
            break
    if 3 in [row_count["X"], col_count["X"], diag1_count["X"], diag2_count["X"]]:
        return "A"
    if 3 in [row_count["O"], col_count["O"], diag1_count["O"], diag2_count["O"]]:
        return "B"
    if global_count[""] > 0:
        return "Pending"
    return "Draw"
    
def check_win(board):
    #In a nxn board, there are n rows, n columns, 2 diagonals
    directions = []
    #Add list of rows
    directions = list(board)
    #Add list of columns
    directions += [[board[rowidx][colidx] for rowidx in range(3)] 
              for colidx in range(3)]
    #Add list of diagonals
    diag1, diag2 = [], []
    for index in range(len(board)):
        diag1 += board[index][index]
        diag2 += board[index][len(board) - 1 - index]
    directions.append(diag1)
    directions.append(diag2)
    empty = 0
    for line in directions:
        if line.count("X") == 3:
            return "A"
        elif line.count("O") == 3:
            return "B"
        else:
            empty += line.count("")
    if empty > 0:
        return "Pending"
    else:
        return "Draw"

def check_win3(board):
    #Add list of rows
    directions = list(board)
    #Add list of columns
    directions += [[board[rowidx][colidx] for rowidx in range(3)] 
              for colidx in range(3)]
    #Add list of diagonals
    diag1, diag2 = [], []
    for index in range(len(board)):
        diag1 += board[index][index]
        diag2 += board[index][len(board) - 1 - index]
    directions.append(diag1)
    directions.append(diag2)
    count = {"X": 0, "O": 0, "": 0}
    for line in directions:
        count["X"] = 0
        count["O"] = 0
        for cell in line:
            count[cell] += 1
        if count["X"] == 3:
            return "A"
        elif count["O"] == 3:
            return "B"
    if count[""] > 0:
        return "Pending"
    else:
        return "Draw"
            
board = [["X","X","X"],
         ["X","O",""],
         ["O","",""]]
#print(check_win(board))
board = [["O","X","O"],
         ["O","X","X"],
         ["X","X","O"]]
#print(check_win(board))
board = [["X","X","O"],
         ["O","O","X"],
         ["X","X","O"]]
#print(check_win(board))
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
output = "A"
print(tictactoe(moves), tictactoe(moves)==output)
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
output = "B"
print(tictactoe(moves), tictactoe(moves)==output)
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
output = "Draw"
print(tictactoe(moves), tictactoe(moves)==output)