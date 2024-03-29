from abc import ABC

from PIL import ImageTk, Image
import dataForChessGame as data
import abc


class chessPiece:
    def __init__(self, color, position, canvas, root, gameScale):
        self.color = color
        self.position = position
        self.canvas = canvas
        self.root = root
        self.gameScale = gameScale
        self.img = None
        self.possibleMoveMarkers = []

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getSprite(self):
        raise NotImplemented

    @abc.abstractmethod
    def validMoves(self, possibleMoveList, allPieces):
        raise NotImplemented

    @abc.abstractmethod
    def possibleMoves(self):
        raise NotImplemented

    def validMoveList(self, allPieces):
        possibleMoveList = self.possibleMoves()
        validMoveList = self.validMoves(possibleMoveList, allPieces)
        return validMoveList

    def placePieces(self):
        self.getSprite()
        pixelValues = self.positionToPixel()
        self.canvas.create_image((pixelValues[0], pixelValues[1]), anchor='center', image=self.img)

    def positionToPixel(self):
        pixelValues = [((((self.position - 1) % 8) + 1) * (self.gameScale / 8)) - (self.gameScale / 16),
                       ((int((self.position - 1) / 8)) * (self.gameScale / 8)) - (3 * self.gameScale / 16) + (
                               self.gameScale / 2)]
        return pixelValues

    def displayPossibleMoves(self, validMoveList, allPieces):
        positionList = validMoveList
        for piece in allPieces:
            if piece.position in positionList:
                marker = possibleMoveMarker(True, piece.position, self.canvas, self.root, self.gameScale)
                marker.placePieces()
                self.possibleMoveMarkers.append(marker)
                positionList.remove(piece.position)
        if positionList:
            for piece in positionList:
                marker = possibleMoveMarker(False, piece, self.canvas, self.root, self.gameScale)
                marker.placePieces()
                self.possibleMoveMarkers.append(marker)
        if not validMoveList:
            print(1)

    @staticmethod
    def resizeImage(inputIMG, factor=int(round(data.gameScale / 8))):
        newIMG = inputIMG.resize((factor, factor), Image.ANTIALIAS)
        return newIMG


class possibleMoveMarker(chessPiece, ABC):
    def getSprite(self):
        if self.color:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\redDot.png'),
                                                           factor=int(round(data.gameScale / 24))))
        elif (((int(self.position / 8 - 0.01) + 1) % 2 == 1) and (self.position % 8) % 2 == 1) or (
                ((int(self.position / 8 - 0.01) + 1) % 2 == 0) and (self.position % 8) % 2 == 0):
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\lightDot.png'),
                                                           factor=int(round(data.gameScale / 24))))
        else:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\darkDot.png'),
                                                           factor=int(round(data.gameScale / 24))))
