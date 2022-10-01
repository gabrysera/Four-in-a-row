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

    def get_value(self, x:int, y:int) -> int:
        """Gets the value of certain coordinate in the board

        Args:
            x (int): x-coordinate
            y (int): y-coordinate

        Returns:
            int: coordinate's value
        """
        return self.board_state[x][y]

    def get_board_state(self) -> list(list(int)):
        """
        Returns:
            list(list(int)): cloned list of the board state
        """
        return [row.copy() for row in self.board_state]

    #player ID make a move in column x
    def play(self, x:int, player_id:int) -> bool:
        """Let player player_id make move in column x

        Args:
            x (int): column
            player_id (int): player to make move

        Returns:
            bool: true if succeeded
        """
        for i in range(len(self.board_state[0])-1, -1, -1): #check column starting from the bottom
            if self.board_state[x][i] == 0:
                self.board_state[x][i] = player_id
                return True
        return False

    #check if a move is valid
    def is_valid(self, x:int) -> bool:
        """Returns if a move is valid or not

        Args:
            x (int): column of the action

        Returns:
            bool: true if spot is not taken yet
        """
        return self.board_state[x][0] == 0

    #Gets a new board given a player and their action (WHY DO WE NEED THIS?)
    def get_new_board(self, col:int, player_id:int) -> Board:
        """Gets a new board given a player and their action

        Args:
            col (int): column of the action
            playerId (int): player that takes the action

        Returns:
            Board: a *new* Board object with the resulting state
        """
        new_board_state = self.get_board_state()
        for i in range(len(new_board_state[0])-1, -1, -1): #check column starting from the bottom
            if new_board_state[col][i] == 0:
                new_board_state[col][i] = player_id
                return Board(board_state = new_board_state) #maybe put a break instead of double return
        return Board(board_state = new_board_state)

    def print_board(self):
        """Draw a human readable representation of the board
        """
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