import string
import chessPieceClasses
import math


class chessGame:
    def __init__(self, white, green, gameScale, canvas, root, FEN):
        self.white = white
        self.green = green
        self.gameScale = gameScale
        self.canvas = canvas
        self.root = root
        self.FEN = FEN

        self.pieceSelected = None

        self.rooks = []
        self.knights = []
        self.bishops = []
        self.queens = []
        self.kings = []
        self.pawns = []
        self.allPieces = ()

    def drawBoard(self):
        rank = 8
        file = 8
        for i in range(rank):
            for j in range(file):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    color = self.green
                else:
                    color = self.white
                x1 = (7 - i) * (self.gameScale / 8)
                y1 = j * (self.gameScale / 8) + (self.gameScale / 4)
                x2 = ((7 - i + 1) * (self.gameScale / 8))
                y2 = ((j + 1) * (self.gameScale / 8)) + (self.gameScale / 4)

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="rect", outline='')

        for i in range(rank):
            if i % 2 == 1:
                color = self.green
            else:
                color = self.white
            x = self.gameScale / 64
            y = (((self.gameScale / 8) * (7 - i + 1)) - (self.gameScale / 10)) + (self.gameScale / 4)
            self.canvas.create_text(x, y, fill=color, text=str(i + 1), font='Helvetica 10 bold')

        for j in range(file):
            if j % 2 == 1:
                color = self.green
            else:
                color = self.white
            x = ((self.gameScale / 8) * (j + 1)) - (self.gameScale / 48)
            y = (self.gameScale - self.gameScale / 48) + (self.gameScale / 4)
            self.canvas.create_text(x, y, fill=color, text=string.ascii_lowercase[j], font='Helvetica 10 bold')

    def processStartFENString(self):
        position = 0
        for x in range(len(self.FEN)):
            if self.FEN[x] in 'rnbqkpRNBQKP':
                position += 1
                if self.FEN[x].isupper():
                    color = 0
                else:
                    color = 1

                if self.FEN[x] in 'rR':
                    self.rooks.append(chessPieceClasses.rook(color, position, canvas=self.canvas, root=self.root,
                                                             gameScale=self.gameScale))
                if self.FEN[x] in 'nN':
                    self.knights.append(chessPieceClasses.knight(color, position, canvas=self.canvas, root=self.root,
                                                                 gameScale=self.gameScale))
                if self.FEN[x] in 'bB':
                    self.bishops.append(chessPieceClasses.bishop(color, position, canvas=self.canvas, root=self.root,
                                                                 gameScale=self.gameScale))
                if self.FEN[x] in 'qQ':
                    self.queens.append(chessPieceClasses.queen(color, position, canvas=self.canvas, root=self.root,
                                                               gameScale=self.gameScale))
                if self.FEN[x] in 'kK':
                    self.kings.append(chessPieceClasses.king(color, position, canvas=self.canvas, root=self.root,
                                                             gameScale=self.gameScale))
                if self.FEN[x] in 'pP':
                    self.pawns.append(chessPieceClasses.pawn(color, position, canvas=self.canvas, root=self.root,
                                                             gameScale=self.gameScale))
            elif self.FEN[x] == '/':
                pass
            else:
                position += int(self.FEN[x])

        self.updateChessPieces()

    def updateChessPieces(self):
        self.allPieces = (self.rooks, self.knights, self.bishops, self.queens, self.kings, self.pawns)
        for x in self.allPieces:
            for y in x:
                y.placePieces()

    def movePiece(self, clickX, clickY):
        clickPosition = (math.ceil((clickY - (self.gameScale / 2)) / self.gameScale * 8) + 1) \
                        + (math.ceil(clickX / self.gameScale * 8)) \
                        + ((math.ceil((clickY - (self.gameScale / 2)) / self.gameScale * 8) + 1) * 7)

        if self.pieceSelected is None:
            for x in self.allPieces:
                for y in x:
                    if y.position == clickPosition:
                        self.pieceSelected = y
        else:
            for x in range(len(self.allPieces)):
                for y in range(len(self.allPieces[x])):
                    if self.allPieces[x][y].position == clickPosition:
                        (self.rooks, self.knights, self.bishops, self.queens, self.kings, self.pawns)[x].remove(
                            (self.rooks, self.knights, self.bishops, self.queens, self.kings, self.pawns)[x][y])
                        break
            self.pieceSelected.position = clickPosition
            self.updateChessPieces()
            self.pieceSelected = None
