from chessPieceClasses import chessPiece
from PIL import ImageTk, Image


class king(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteKing.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackKing.png')))


    def possibleMoves(self):
        possibleMoveList = []
        # Calculate the king moves.
        x, y = divmod(self.position - 1, 8)
        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
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
