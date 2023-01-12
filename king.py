from chessPieceClasses import chessPiece
from PIL import ImageTk, Image


class king(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteKing.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackKing.png')))
