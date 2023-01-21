import tkinter as tk
from chessGame import chessGame
import dataForChessGame as data
from dataForChessGame import gameScale


class initialize(object):
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=gameScale, height=int(gameScale + gameScale / 2), highlightthickness=0,
                                background=data.brown)

        # Changing the startFEN changes the starting position
        self.c = chessGame(white=data.white, green=data.green, gameScale=data.gameScale, canvas=self.canvas,
                           root=self.root,
                           FEN=data.startFEN)

    def main(self):
        self.root.title("chessGame")
        self.root.configure(background='Black')
        self.root.geometry(f'{str(gameScale)}x{str(int(gameScale + gameScale / 2))}')

        self.c.drawBoard()
        self.c.processStartFENString()

        self.canvas.pack()
        self.root.mainloop()


i = initialize()
i.main()
