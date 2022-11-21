from PIL import ImageTk, Image
import dataForChessGame as data


class chessPiece:
    def __init__(self, color, position, canvas, root, gameScale):
        self.color = color
        self.position = position
        self.canvas = canvas
        self.root = root
        self.gameScale = gameScale
        self.img = None

    def getSprite(self):
        pass

    def placePieces(self):
        self.getSprite()
        pixelValues = self.positionToPixel()
        self.canvas.create_image((pixelValues[0], pixelValues[1]), anchor='center', image=self.img)

    def positionToPixel(self):
        pixelValues = [((((self.position - 1) % 8) + 1) * (self.gameScale / 8)) - (self.gameScale / 16),
                       ((int((self.position - 1) / 8)) * (self.gameScale / 8)) - (3 * self.gameScale / 16) + (
                               self.gameScale / 2)]
        return pixelValues

    @staticmethod
    def resizeImage(inputIMG):
        newIMG = inputIMG.resize((int(round(data.gameScale / 8)), int(round(data.gameScale / 8))), Image.ANTIALIAS)
        return newIMG


class rook(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteRook.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackRook.png')))


class knight(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteKnight.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackKnight.png')))


class bishop(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteBishop.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackBishop.png')))


class queen(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteQueen.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackQueen.png')))


class king(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whiteKing.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackKing.png')))


class pawn(chessPiece):
    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whitePawn.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackPawn.png')))
