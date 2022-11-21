import string
import tkinter as tk
import chessPieceClasses
from tkinter import *
from PIL import ImageTk, Image

import dataForChessGame as data
from dataForChessGame import gameScale


def initialize():
    root = tk.Tk()
    root.title("chessGame")
    root.configure(background='Black')
    root.geometry(f'{str(gameScale)}x{str(int(gameScale + gameScale / 2))}')
    canvas = tk.Canvas(root, width=gameScale, height=int(gameScale + gameScale / 2), highlightthickness=0,
                       background=data.brown)

    createBoard(canvas)
    placePieces(canvas, root)

    # Can set preset positions here using a var with FEN

    canvas.pack()
    root.mainloop()


def createBoard(canvas):
    rank = 8
    file = 8
    for i in range(rank):
        for j in range(file):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                color = data.green
            else:
                color = data.white
            x1 = (7 - i) * (gameScale / 8)
            y1 = j * (gameScale / 8) + (gameScale / 4)
            x2 = ((7 - i + 1) * (gameScale / 8))
            y2 = ((j + 1) * (gameScale / 8)) + (gameScale / 4)

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="rect", outline='')

    for i in range(rank):
        if i % 2 == 1:
            color = data.green
        else:
            color = data.white
        x = gameScale / 64
        y = (((gameScale / 8) * (7 - i + 1)) - (gameScale / 10)) + (gameScale / 4)
        canvas.create_text(x, y, fill=color, text=str(i + 1), font='Helvetica 10 bold')

    for j in range(file):
        if j % 2 == 1:
            color = data.green
        else:
            color = data.white
        x = ((gameScale / 8) * (j + 1)) - (gameScale / 48)
        y = (gameScale - gameScale / 48) + (gameScale / 4)
        canvas.create_text(x, y, fill=color, text=string.ascii_lowercase[j], font='Helvetica 10 bold')


def placePieces(canvas, root):
    canvas.pack()
    rook = chessPieceClasses.rook(0, 1)
    img = rook.getSprite()
    root.img = img
    canvas.create_image((10, 10), anchor=NW, image=img)


initialize()
