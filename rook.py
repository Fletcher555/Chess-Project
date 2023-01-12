import math
from chessPieceClasses import chessPiece
from PIL import ImageTk, Image


class rook(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteRook.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackRook.png')))

    def possibleMoves(self):
        possibleMoveList = []
        # This for loop calculates all the possible moves along the files.
        for x in range(8):
            if ((self.position - 1) % 8 + 1) + (8 * x) != self.position:
                possibleMoveList.append(((self.position - 1) % 8 + 1) + (8 * x))
        # This for loop calculates all the possible moves along the ranks.
        for x in range(8):
            if (math.ceil(self.position / 8) - 1) * 8 + x + 1 != self.position:
                possibleMoveList.append((math.ceil(self.position / 8) - 1) * 8 + x + 1)
        return possibleMoveList

    def validMoves(self, possibleMoveList, allPieces):
        validMoveList = possibleMoveList
        # This takes the list of all the possible moves and finds the valid moves.
        for x in allPieces:
            if x.position in validMoveList:
                # After checking if there is a piece in one of the possible move squares we check if it is in the same file or rank.
                if x.position % 8 == self.position % 8:
                    # Here if it is the same file we check whether the piece is above or below the current piece and based on this we remove pieces.
                    # This makes sure there is no leap frogging.
                    if self.position > x.position:
                        validMoveList = [y for y in validMoveList if y >= x.position]
                    elif self.position < x.position:
                        validMoveList = [y for y in validMoveList if y <= x.position]
                # This checks if there is a piece in the same rank.
                elif math.ceil(self.position / 8) == math.ceil(x.position / 8):
                    if self.position > x.position:
                        # The list comprehension here adds a check to make sure it doesn't remove file moves.
                        validMoveList = [y for y in validMoveList if y >= x.position or y <= self.position - 8]
                    elif self.position < x.position:
                        validMoveList = [y for y in validMoveList if y <= x.position or y >= self.position + 8]
                # This checks if the piece is the same color if it is then it removes that as a possible move.
                if x.color == self.color:
                    validMoveList.remove(x.position)
        return validMoveList
