from chessPieceClasses import chessPiece
from PIL import ImageTk, Image
import math


class queen(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteQueen.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackQueen.png')))

    def possibleMoves(self):
        possibleMoveList = []

        # Calculate the queen moves.
        x, y = divmod(self.position - 1, 8)
        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    possibleMoveList.append(new_x * 8 + new_y + 1)
                else:
                    break

        return possibleMoveList

    def validMoves(self, possibleMoveList, allPieces):
        validMoveList = possibleMoveList
        # Calculates row and column of self
        positionColumn = (self.position - 1) % 8 + 1
        positionRow = math.ceil(self.position / 8)

        for x in allPieces:
            # Calculates row and column of piece in sight
            xPositionColumn = (x.position - 1) % 8 + 1
            xPositionRow = math.ceil(x.position / 8)
            if x != self:
                # Checks all rook moves for comments see rook class.
                if positionRow == xPositionRow:
                    if positionColumn > xPositionColumn:
                        validMoveList = [y for y in validMoveList if
                                         math.ceil(y / 8) != xPositionRow or ((y - 1) % 8 + 1) >= xPositionColumn]
                    elif positionColumn < xPositionColumn:
                        validMoveList = [y for y in validMoveList if
                                         math.ceil(y / 8) != xPositionRow or ((y - 1) % 8 + 1) <= xPositionColumn]
                elif positionColumn == xPositionColumn:
                    if positionRow > xPositionRow:
                        validMoveList = [y for y in validMoveList if
                                         ((y - 1) % 8 + 1) != xPositionColumn or math.ceil(y / 8) >= xPositionRow]
                    elif positionRow < xPositionRow:
                        validMoveList = [y for y in validMoveList if
                                         ((y - 1) % 8 + 1) != xPositionColumn or math.ceil(y / 8) <= xPositionRow]

                # Checks all bishop moves for comments see bishop class.
                if x.position in validMoveList:
                    if xPositionRow > positionRow:
                        if xPositionColumn > positionColumn:
                            validMoveList = [y for y in validMoveList if
                                             ((y - 1) % 8 + 1) <= xPositionColumn or math.ceil(y / 8) <= xPositionRow]
                        elif xPositionColumn < positionColumn:
                            validMoveList = [y for y in validMoveList if
                                             ((y - 1) % 8 + 1) >= xPositionColumn or math.ceil(y / 8) <= xPositionRow]
                    if xPositionRow < positionRow:
                        if xPositionColumn > positionColumn:
                            validMoveList = [y for y in validMoveList if
                                             ((y - 1) % 8 + 1) <= xPositionColumn or math.ceil(y / 8) >= xPositionRow]
                        elif xPositionColumn < positionColumn:
                            validMoveList = [y for y in validMoveList if
                                             ((y - 1) % 8 + 1) >= xPositionColumn or math.ceil(y / 8) >= xPositionRow]
            if x.position in validMoveList:
                if x.color == self.color:
                    validMoveList.remove(x.position)

        return validMoveList
