import string
import math
from chessPieces.pawn import pawn
from chessPieces.knight import knight
from chessPieces.bishop import bishop
from chessPieces.queen import queen
from chessPieces.rook import rook
from chessPieces.king import king


class chessGame:
    def __init__(self, white, green, gameScale, canvas, root, FEN):

        canvas.bind("<Button-1>", self.callback)
        canvas.bind('<Button1-Motion>', self.move)
        canvas.bind('<ButtonRelease-1>', self.release)

        self.white = white
        self.green = green
        self.gameScale = gameScale
        self.canvas = canvas
        self.root = root
        self.FEN = FEN

        self.pieceSelected = None
        self.allPieces = []

    def move(self, event):
        pass

    def release(self, event):
        pass

    def callback(self, event):
        if event.y > self.gameScale / 4:
            self.movePiece(clickX=event.x, clickY=event.y)

    def drawBoard(self):
        for rank in range(8):
            for file in range(8):
                if (rank % 2 == 0 and file % 2 == 0) or (rank % 2 == 1 and file % 2 == 1):
                    color = self.green
                else:
                    color = self.white
                x1 = (7 - rank) * (self.gameScale / 8)
                y1 = file * (self.gameScale / 8) + (self.gameScale / 4)
                x2 = ((7 - rank + 1) * (self.gameScale / 8))
                y2 = ((file + 1) * (self.gameScale / 8)) + (self.gameScale / 4)

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="rect", outline='')

        for rank in range(8):
            if rank % 2 == 1:
                color = self.green
            else:
                color = self.white
            x = self.gameScale / 64
            y = (((self.gameScale / 8) * (7 - rank + 1)) - (self.gameScale / 10)) + (self.gameScale / 4)
            self.canvas.create_text(x, y, fill=color, text=str(rank + 1), font='Helvetica 10 bold')

        for file in range(8):
            if file % 2 == 1:
                color = self.green
            else:
                color = self.white
            x = ((self.gameScale / 8) * (file + 1)) - (self.gameScale / 48)
            y = (self.gameScale - self.gameScale / 48) + (self.gameScale / 4)
            self.canvas.create_text(x, y, fill=color, text=string.ascii_lowercase[file], font='Helvetica 10 bold')

    def processStartFENString(self):
        position = 0
        for letter in self.FEN:
            if letter in 'rnbqkpRNBQKP':
                position += 1
                if letter.isupper():
                    color = 0  # White
                else:
                    color = 1  # Black

                if letter in 'rR':
                    self.allPieces.append(rook(color, position, canvas=self.canvas, root=self.root,
                                               gameScale=self.gameScale))
                if letter in 'nN':
                    self.allPieces.append(knight(color, position, canvas=self.canvas, root=self.root,
                                                 gameScale=self.gameScale))
                if letter in 'bB':
                    self.allPieces.append(bishop(color, position, canvas=self.canvas, root=self.root,
                                                 gameScale=self.gameScale))
                if letter in 'qQ':
                    self.allPieces.append(queen(color, position, canvas=self.canvas, root=self.root,
                                                gameScale=self.gameScale))
                if letter in 'kK':
                    self.allPieces.append(king(color, position, canvas=self.canvas, root=self.root,
                                               gameScale=self.gameScale))
                if letter in 'pP':
                    self.allPieces.append(pawn(color, position, canvas=self.canvas, root=self.root,
                                               gameScale=self.gameScale))
            elif letter != '/':
                position += int(letter)

        self.updateChessPieces()

    def updateChessPieces(self, oldPos=None):

        for piece in self.allPieces:
            piece.placePieces()

            # Removes all old en passant
            if type(piece).__name__ == "pawn":
                piece.isEnPassant = False

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
            for piece in self.allPieces:
                if piece.position == clickPosition:
                    self.pieceSelected = piece
                    validMoveList = self.pieceSelected.validMoveList(self.allPieces)
                    # If the list is empty, i.e. the piece has no possible moves it will be unselected
                    if not validMoveList:
                        self.pieceSelected = None
                    else:
                        self.pieceSelected.displayPossibleMoves(validMoveList, self.allPieces)

        else:
            if clickPosition in self.pieceSelected.validMoveList(self.allPieces):
                for i, piece in enumerate(self.allPieces):
                    if piece.position == clickPosition:
                        del self.allPieces[i]
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
                        for i, piece in enumerate(self.allPieces):
                            if type(piece).__name__ == "pawn" and piece.isEnPassant:
                                if self.pieceSelected.color == 0 and piece.position - self.pieceSelected.position == 8:
                                    del self.allPieces[i]
                                    break
                    self.updateChessPieces(oldPos)

            else:
                self.updateChessPieces()
