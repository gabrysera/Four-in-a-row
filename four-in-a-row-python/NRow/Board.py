from __future__ import annotations

class Board:

    #constructor
    def __init__(self, width:int = 0, height:int = 0, board:Board = None, board_state:list(list(int)) = [[]]):
        if board is not None:
            self.__set_board_parameters(board.width, board.height, board.get_board_state())
        elif board_state != [[]]:
            self.__set_board_parameters(len(board_state), len(board_state[0]), board_state)
        else:
            self.__set_board_parameters(width, height, [[0 for x in range(height)] for y in range(width)])
    
    #function used to abstract different constructors
    def __set_board_parameters(self, width:int = 0, height:int = 0, board_state:list(list(int)) = []):
        self.width = width
        self.height = height
        self.board_state = board_state

    #get value in a certain coordinate
    def get_value(self, x:int, y:int) -> int:
        return self.board_state[x][y]

    #get a copy of the state
    def get_board_state(self) -> list(list(int)):
        return [row.copy() for row in self.board_state]

    #player ID make a move in column x
    def play(self, x:int, playerId:int) -> bool:
        for i in range(len(self.board_state[0])-1, -1, -1): #check column starting from the bottom
            if self.board_state[x][i] == 0:
                self.board_state[x][i] = playerId
                return True
        return False

    #check if a move is valid
    def is_valid(self, x:int) -> bool:
        return self.board_state[x][0] == 0

    #Gets a new board given a player and their action (WHY DO WE NEED THIS?)
    def get_new_board(self, col:int, playerId:int) -> Board:
        new_board_state = self.get_board_state()
        for i in range(len(new_board_state[0])-1, -1, -1): #check column starting from the bottom
            if new_board_state[col][i] == 0:
                new_board_state[col][i] = playerId
                return Board(board_state = new_board_state) #maybe put a break instead of double return
        return Board(board_state = new_board_state)

    #print board
    def print_board(self):
        divider = " "
        divider2 = " "
        number_row = "|"
        output = ""
        for i in range(0, len(self.board_state)):
            divider += "--- "
            divider2 += "==="
            number_row += " " + (str(i + 1)) + " |"
        
        for i in range(0, len(self.board_state[0])):
            output += "\n" + divider + "\n"
            for j in range(0, len(self.board_state)):
                node = " "
                if self.board_state[j][i] == 1:
                    node = "X"
                elif self.board_state[j][i] == 2:
                    node = "O"
                output += "| " + node + " "
            output += "|"
        output += "\n" + divider2 + "\n" + number_row + "\n"
        print(output)