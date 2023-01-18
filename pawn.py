from chessPieceClasses import chessPiece
from PIL import ImageTk, Image


class pawn(chessPiece):
    # This is a property of only the pawn class, if set to true this pawn can be taken en passant.
    # Is controlled by chessGame function.
    isEnPassant = False

    def getSprite(self):
        if self.color == 0:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\whitePawn.png')))
        elif self.color == 1:
            self.img = ImageTk.PhotoImage(self.resizeImage(Image.open(r'chessSprites\blackPawn.png')))

    def possibleMoves(self):
        possibleMoveList = []
        if self.color == 0:  # White
            # If the pawn is in the start position it can move two spaces otherwise only one
            if self.position in [49, 50, 51, 52, 53, 54, 55, 56]:
                possibleMoveList = [self.position - 8, self.position - 16]
            else:
                possibleMoveList = [self.position - 8]
        elif self.color == 1:  # Black
            # If the pawn is in the start position it can move two spaces otherwise only one
            if self.position in [9, 10, 11, 12, 13, 14, 15, 16]:
                possibleMoveList = [self.position + 8, self.position + 16]
            else:
                possibleMoveList = [self.position + 8]

        return possibleMoveList

    def validMoves(self, possibleMoveList, allPieces):
        validMoveList = possibleMoveList
        for x in allPieces:
            # White
            if self.color == 0:
                # If there is a piece in front of the pawn.
                if self.position - x.position == 8:
                    validMoveList.remove(x.position)
                    # If there is a piece in front of the pawn also remove the double jump if it is there.
                    if self.position - 16 in validMoveList:
                        validMoveList.remove(self.position - 16)
                # If the potential piece is the opposite color.
                if self.color != x.color:
                    # If the potential piece is to the left add that as a possible move.
                    if self.position - 9 == x.position and self.position % 8 != 1:
                        validMoveList.append(self.position - 9)
                    # If the potential piece is to the right add that as a possible move.
                    elif self.position - 7 == x.position and self.position % 8 != 0:
                        validMoveList.append(self.position - 7)

                    # This allows for en passant captures based on the variable stored by the pawn object.
                    elif self.position - 1 == x.position and self.position % 8 != 0:
                        if type(x).__name__ == "pawn":
                            if x.isEnPassant:
                                validMoveList.append(self.position - 9)
                    elif self.position + 1 == x.position and self.position % 8 != 1:
                        if type(x).__name__ == "pawn":
                            if x.isEnPassant:
                                validMoveList.append(self.position - 7)

            # Black
            if self.color == 1:
                # If there is a piece in front of the pawn.
                if x.position - self.position == 8:
                    validMoveList.remove(x.position)
                    # If there is a piece in front of the pawn also remove the double jump if it is there.
                    if self.position + 16 in validMoveList:
                        validMoveList.remove(self.position + 16)
                # If the potential piece is the opposite color.
                if self.color != x.color:
                    # If the potential piece is to the right add that as a possible move.
                    if self.position + 9 == x.position and self.position % 8 != 0:
                        validMoveList.append(self.position + 9)
                        # If the potential piece is to the left add that as a possible move.
                    elif self.position + 7 == x.position and self.position % 8 != 1:
                        validMoveList.append(self.position + 7)

                    # This allows for en passant captures based on the variable stored by the pawn object.
                    elif self.position + 1 == x.position and self.position % 8 != 0:
                        if type(x).__name__ == "pawn":
                            if x.isEnPassant:
                                validMoveList.append(self.position + 9)
                    elif self.position - 1 == x.position and self.position % 8 != 1:
                        if type(x).__name__ == "pawn":
                            if x.isEnPassant:
                                validMoveList.append(self.position + 7)

        return validMoveList
