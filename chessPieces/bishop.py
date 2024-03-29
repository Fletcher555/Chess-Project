from chessPiece import chessPiece
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
        x, y = divmod(self.position - 1, 8)
        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    possibleMoveList.append(new_x * 8 + new_y + 1)
                else:
                    break
        return possibleMoveList

    def validMoves(self, possibleMoveList, allPieces):
        validMoveList = possibleMoveList
        # These two formulas calculate the row and column of the bishop
        positionColumn = (self.position - 1) % 8 + 1
        positionRow = math.ceil(self.position / 8)

        for piece in allPieces:
            if piece != self:
                if piece.position in validMoveList:
                    # Calculates row and column of piece in sight
                    xPositionColumn = (piece.position - 1) % 8 + 1
                    xPositionRow = math.ceil(piece.position / 8)

                    # If the piece is below.
                    if xPositionRow > positionRow:
                        # If piece is bottom right.
                        if xPositionColumn > positionColumn:
                            validMoveList = [validMove for validMove in validMoveList if ((validMove - 1) % 8 + 1) <= xPositionColumn or math.ceil(validMove / 8) <= xPositionRow]
                        # If piece is bottom left.
                        elif xPositionColumn < positionColumn:
                            validMoveList = [validMove for validMove in validMoveList if ((validMove - 1) % 8 + 1) >= xPositionColumn or math.ceil(validMove / 8) <= xPositionRow]
                    # If piece is above.
                    if xPositionRow < positionRow:
                        # If piece is top right.
                        if xPositionColumn > positionColumn:
                            validMoveList = [validMove for validMove in validMoveList if ((validMove - 1) % 8 + 1) <= xPositionColumn or math.ceil(validMove / 8) >= xPositionRow]
                        # If piece is top left.
                        elif xPositionColumn < positionColumn:
                            validMoveList = [validMove for validMove in validMoveList if ((validMove - 1) % 8 + 1) >= xPositionColumn or math.ceil(validMove / 8) >= xPositionRow]
            if piece.position in validMoveList:
                if piece.color == self.color:
                    validMoveList.remove(piece.position)

        return validMoveList
