import math
from chessPiece import chessPiece
from PIL import ImageTk, Image


class rook(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteRook.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackRook.png')))

    def possibleMoves(self):
        possibleMoveList = []
        x, y = divmod(self.position - 1, 8)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
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
        for piece in allPieces:
            # Calculates row and column of piece in sight
            xPositionColumn = (piece.position - 1) % 8 + 1
            xPositionRow = math.ceil(piece.position / 8)
            if piece != self:
                if positionRow == xPositionRow:
                    if positionColumn > xPositionColumn:
                        validMoveList = [validMove for validMove in validMoveList if math.ceil(validMove / 8) != xPositionRow or ((validMove - 1) % 8 + 1) >= xPositionColumn]
                    elif positionColumn < xPositionColumn:
                        validMoveList = [validMove for validMove in validMoveList if math.ceil(validMove / 8) != xPositionRow or ((validMove - 1) % 8 + 1) <= xPositionColumn]

                elif positionColumn == xPositionColumn:
                    if positionRow > xPositionRow:
                        validMoveList = [validMove for validMove in validMoveList if((validMove - 1) % 8 + 1) != xPositionColumn or math.ceil(validMove / 8) >= xPositionRow]
                    elif positionRow < xPositionRow:
                        validMoveList = [validMove for validMove in validMoveList if((validMove - 1) % 8 + 1) != xPositionColumn or math.ceil(validMove / 8) <= xPositionRow]
            if piece.position in validMoveList:
                if piece.color == self.color:
                    validMoveList.remove(piece.position)
        return validMoveList
