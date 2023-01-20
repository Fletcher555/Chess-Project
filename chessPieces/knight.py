from chessPieceClasses import chessPiece
from PIL import ImageTk, Image


class knight(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteKnight.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackKnight.png')))

    def possibleMoves(self):
        possibleMoveList = []
        # Calculate the king moves.
        x, y = divmod(self.position - 1, 8)
        for dx, dy in [(2, 1), (2, -1), (-1, 2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                possibleMoveList.append(new_x * 8 + new_y + 1)

        return possibleMoveList

    def validMoves(self, possibleMoveList, allPieces):
        validMoveList = possibleMoveList
        for x in allPieces:
            if x.color == self.color:
                if x.position in validMoveList:
                    validMoveList.remove(x.position)
        return validMoveList

