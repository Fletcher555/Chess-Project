from chessPieceClasses import chessPiece
from PIL import ImageTk, Image
import math


class bishop(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteBishop.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackBishop.png')))

    def possibleMoves(self):
        possibleMoveList = []
        # Checks to see if the bishop is on the right edge of the board.
        # This whole if statement handles the pieces moving right.
        if self.position % 8 != 0:
            # This adds all the values to the top right direction.
            x = 0
            while self.position + (x + 1) - ((x + 1) * 8) > 1:
                possibleMoveList.append(self.position + (x + 1) - ((x + 1) * 8))
                if ((self.position + (x + 1) - ((x + 1) * 8)) % 8) == 0:
                    break
                x += 1
            # This adds all the values to the bottom right.
            x = 0
            while self.position + ((x + 1) * 8) + (1 + x) <= 64:
                possibleMoveList.append(self.position + ((x + 1) * 8) + (1 + x))
                if (self.position + ((x + 1) * 8) + (1 + x)) % 8 == 0:
                    break
                x += 1
        # Checks to see if the bishop is on the left edge of the board.
        # This whole if statement handles the pieces moving left.
        if self.position % 8 != 1:
            # This adds all the values to the bottom left direction.
            x = 0
            while (self.position - (x + 1) + ((x + 1) * 8)) < 64:
                possibleMoveList.append(self.position - (x + 1) + ((x + 1) * 8))
                if (self.position - (x + 1) + ((x + 1) * 8)) % 8 == 1:
                    break
                x += 1
            # This adds all the values in the top left direction.
            x = 0
            while self.position - ((x + 1) * 8) - (1 + x) > 0:
                possibleMoveList.append(self.position - ((x + 1) * 8) - (1 + x))
                if (self.position - ((x + 1) * 8) - (1 + x)) % 8 == 1:
                    break
                x += 1

        return possibleMoveList

    def validMoves(self, possibleMoveList, allPieces):
        validMoveList = possibleMoveList
        # These two formulas calculate the row and column of the bishop
        positionColumn = (self.position - 1) % 8 + 1
        positionRow = math.ceil(self.position / 8)

        for x in allPieces:
            if x != self:
                if x.position in validMoveList:
                    # Calculates row and column of piece in sight
                    xPositionColumn = (x.position - 1) % 8 + 1
                    xPositionRow = math.ceil(x.position / 8)

                    # If the piece is below.
                    if xPositionRow > positionRow:
                        # If piece is bottom right.
                        if xPositionColumn > positionColumn:
                            validMoveList = [y for y in validMoveList if ((y - 1) % 8 + 1) <= xPositionColumn or math.ceil(y / 8) <= xPositionRow]
                        # If piece is bottom left.
                        elif xPositionColumn < positionColumn:
                            validMoveList = [y for y in validMoveList if ((y - 1) % 8 + 1) >= xPositionColumn or math.ceil(y / 8) <= xPositionRow]
                    # If piece is above.
                    if xPositionRow < positionRow:
                        # If piece is top right.
                        if xPositionColumn > positionColumn:
                            validMoveList = [y for y in validMoveList if ((y - 1) % 8 + 1) <= xPositionColumn or math.ceil(y / 8) >= xPositionRow]
                        # If piece is top left.
                        elif xPositionColumn < positionColumn:
                            validMoveList = [y for y in validMoveList if ((y - 1) % 8 + 1) >= xPositionColumn or math.ceil(y / 8) >= xPositionRow]
            if x.position in validMoveList:
                if x.color == self.color:
                    validMoveList.remove(x.position)

        return validMoveList
