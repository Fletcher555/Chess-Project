from chessPieceClasses import chessPiece
from PIL import ImageTk, Image


class pawn(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whitePawn.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackPawn.png')))
