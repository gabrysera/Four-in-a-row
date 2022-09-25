from __future__ import annotations

class Board:

    #constructor
    def __init__(self, width:int = 0, height:int = 0, board:Board = None, boardState:list(list(int)) = [[]]):
        if board is not None:
            self.__setBoardParameters(board.width, board.height, board.getBoardState())
        elif boardState != [[]]:
            self.__setBoardParameters(len(boardState), len(boardState[0]), boardState)
        else:
            self.__setBoardParameters(width, height, [[0 for x in range(height)] for y in range(width)])
    
    #function used to abstract different constructors
    def __setBoardParameters(self, width:int = 0, height:int = 0, boardState:list(list(int)) = []):
        self.width = width
        self.height = height
        self.boardState = boardState

    #get value in a certain coordinate
    def getValue(self, x:int, y:int) -> int:
        return self.boardState[x][y]

    #get a copy of the state
    def getBoardState(self) -> list(list(int)):
        return [row.copy() for row in self.boardState]

    #player ID make a move in column x
    def play(self, x:int, playerId:int) -> bool:
        for i in range(len(self.boardState[0])-1, 0, -1): #check column starting from the bottom
            if self.boardState[x][i] == 0:
                self.boardState[x][i] = playerId
                print("how many times here")
                return True
        return False

    #check if a move is valid
    def isValid(self, x:int) -> bool:
        return self.boardState[x][0] == 0

    #Gets a new board given a player and their action (WHY DO WE NEED THIS?)
    def getNewBoard(self, x:int, playerId:int) -> Board:
        newBoardState = self.getBoardState()
        for i in range(len(newBoardState[0])-1, 0, -1): #check column starting from the bottom
            if newBoardState[x][i] == 0:
                self.boardState[x][i] = playerId
                return Board(boardState = newBoardState) #maybe put a break instead of double return
        return Board(boardState = newBoardState)

    #print board
    def printBoard(self):
        divider = " "
        divider2 = " "
        numberRow = "|"
        output = ""
        for i in range(0, len(self.boardState)):
            divider += "--- "
            divider2 += "==="
            numberRow += " " + (str(i + 1)) + " |"
        
        for i in range(0, len(self.boardState[0])):
            output += "\n" + divider + "\n"
            for j in range(0, len(self.boardState)):
                node = " "
                if self.boardState[j][i] == 1:
                    node = "X"
                elif self.boardState[j][i] == 2:
                    node = "O"
                output += "| " + node + " "
            output += "|"
        output += "\n" + divider2 + "\n" + numberRow + "\n"
        print(output)