import tkinter as tk
from chessGame import chessGame
import time
import dataForChessGame as data
from dataForChessGame import gameScale


class initialize(object):
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=gameScale, height=int(gameScale + gameScale / 2), highlightthickness=0,
                                background=data.brown)
        self.c = chessGame(white=data.white, green=data.green, gameScale=data.gameScale, canvas=self.canvas,
                           root=self.root,
                           FEN=data.startFEN)



    def main(self):
        self.root.title("chessGame")
        self.root.configure(background='Black')
        self.root.geometry(f'{str(gameScale)}x{str(int(gameScale + gameScale / 2))}')

        self.c.drawBoard()
        self.c.processStartFENString()



        # Can set preset positions here using a var with FEN

        self.canvas.pack()
        self.root.mainloop()
        time.sleep(3)




i = initialize()

i.main()
