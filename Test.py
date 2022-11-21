def movePiece(self, clickX, clickY):
    clickPosition = (math.ceil((clickY - (self.gameScale / 2)) / self.gameScale * 8) + 1) \
                    + (math.ceil(clickX / self.gameScale * 8)) \
                    + ((math.ceil((clickY - (self.gameScale / 2)) / self.gameScale * 8) + 1) * 7)

    print(self.pieceSelected)

    for x in range(len(self.allPieces)):
        for y in range(len(self.allPieces[x])):
            if self.allPieces[x][y].position == clickPosition:
                if self.pieceSelected is None:
                    print("selected")
                    self.pieceSelected = self.allPieces[x][y]
                    print(self.pieceSelected)

            else:
                print("moved")
                (self.rooks, self.knights, self.bishops, self.queens, self.kings, self.pawns)[x].remove(
                    (self.rooks, self.knights, self.bishops, self.queens, self.kings, self.pawns)[x][y])
                self.pieceSelected.position = clickPosition
                self.updateChessPieces()
                self.pieceSelected = None
                break