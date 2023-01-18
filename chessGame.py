import string
import math
from pawn import pawn
from knight import knight
from bishop import bishop
from queen import queen
from rook import rook
from king import king


class chessGame:
    def __init__(self, white, green, gameScale, canvas, root, FEN):
        self.white = white
        self.green = green
        self.gameScale = gameScale
        self.canvas = canvas
        self.root = root
        self.FEN = FEN

        self.pieceSelected = None
        self.allPieces = []

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
                    color = 0  # White
                else:
                    color = 1  # Black

                if self.FEN[x] in 'rR':
                    self.allPieces.append(rook(color, position, canvas=self.canvas, root=self.root,
                                               gameScale=self.gameScale))
                if self.FEN[x] in 'nN':
                    self.allPieces.append(knight(color, position, canvas=self.canvas, root=self.root,
                                                 gameScale=self.gameScale))
                if self.FEN[x] in 'bB':
                    self.allPieces.append(bishop(color, position, canvas=self.canvas, root=self.root,
                                                 gameScale=self.gameScale))
                if self.FEN[x] in 'qQ':
                    self.allPieces.append(queen(color, position, canvas=self.canvas, root=self.root,
                                                gameScale=self.gameScale))
                if self.FEN[x] in 'kK':
                    self.allPieces.append(king(color, position, canvas=self.canvas, root=self.root,
                                               gameScale=self.gameScale))
                if self.FEN[x] in 'pP':
                    self.allPieces.append(pawn(color, position, canvas=self.canvas, root=self.root,
                                               gameScale=self.gameScale))
            elif self.FEN[x] == '/':
                pass
            else:
                position += int(self.FEN[x])

        self.updateChessPieces()

    def updateChessPieces(self, oldPos=None):

        for x in self.allPieces:
            x.placePieces()

            # Removes all old en passant
            if type(x).__name__ == "pawn":
                x.isEnPassant = False

        # If last move was a double forward it makes that pawn be able to be taken en passant
        if type(self.pieceSelected).__name__ == "pawn":
            if oldPos is not None:
                if abs(self.pieceSelected.position - oldPos) == 16:
                    if self.pieceSelected.color == 0:
                        self.pieceSelected.isEnPassant = True
                    elif self.pieceSelected.color == 1:
                        self.pieceSelected.isEnPassant = True

        if self.pieceSelected is not None:
            self.pieceSelected.possibleMoveMarkers = []
            self.pieceSelected = None

    def movePiece(self, clickX, clickY):
        clickPosition = (math.ceil((clickY - (self.gameScale / 2)) / self.gameScale * 8) + 1) \
                        + (math.ceil(clickX / self.gameScale * 8)) \
                        + ((math.ceil((clickY - (self.gameScale / 2)) / self.gameScale * 8) + 1) * 7)

        if self.pieceSelected is None:
            for x in self.allPieces:
                if x.position == clickPosition:
                    self.pieceSelected = x
                    validMoveList = self.pieceSelected.validMoveList(self.allPieces)
                    # If the list is empty, i.e. the piece has no possible moves it will be unselected
                    if not validMoveList:
                        self.pieceSelected = None
                    else:
                        self.pieceSelected.displayPossibleMoves(validMoveList, self.allPieces)

        else:
            if clickPosition in self.pieceSelected.validMoveList(self.allPieces):
                for x in range(len(self.allPieces)):
                    if self.allPieces[x].position == clickPosition:
                        del self.allPieces[x]
                        oldPos = self.pieceSelected.position
                        self.pieceSelected.position = clickPosition
                        self.updateChessPieces(oldPos)
                        break
                else:
                    oldPos = self.pieceSelected.position
                    self.pieceSelected.position = clickPosition
                    # The check below is for an en passant take, this is the only time a piece is deleted without the
                    # capturing piece being in the same square.
                    if type(self.pieceSelected).__name__ == "pawn":
                        for x in range(len(self.allPieces)):
                            if type(self.allPieces[x]).__name__ == "pawn" and abs(
                                    self.allPieces[x].position - self.pieceSelected.position) == 8 and self.allPieces[x].isEnPassant:
                                print(1)
                                del self.allPieces[x]
                                break
                    self.updateChessPieces(oldPos)

            else:
                self.updateChessPieces()
