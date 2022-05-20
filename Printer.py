import numpy as np
from Definitions import *

# White Pieces
Pawn = Piece(1)
Bishop = Piece(2)
Knight = Piece(3)
Rook = Piece(4)
Queen = Piece(5)
King = Piece(6)

# Black Pieces
PawnB = Piece(7)
BishopB = Piece(8)
KnightB = Piece(9)
RookB = Piece(10)
QueenB = Piece(11)
KingB = Piece(12)

def Printer(Pieces, Board):
    Green = 0.45
    Brown = 0.81
    Yellow = 0.7

    # Pieces to Board Generator
    for py in range(8):
        for px in range(8):
            if Pieces[py,px] == 0:
                for Bx in range(7):
                    for By in range(7):
                        # if Board[py*9+By+1,px*9+Bx+1] != 1 and Board[py*9+By+1,px*9+Bx+1] != 0:
                        Board[py*9+By+1,px*9+Bx+1] = 0.75
            # if Pieces[py,px] == 0.069:
            #     for Bx in range(7):
            #         for By in range(7):
            #             Board[py*9+By+1,px*9+Bx+1] = Yellow
            #     # Pieces[py,px] = 0
            if Pieces[py,px] == 1:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = Pawn[By,Bx]
            if Pieces[py,px] == 2:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = Bishop[By,Bx]
            if Pieces[py,px] == 3:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = Knight[By,Bx]
            if Pieces[py,px] == 4:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = Rook[By,Bx]
            if Pieces[py,px] == 5:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = Queen[By,Bx]
            if Pieces[py,px] == 6:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = King[By,Bx]
            if Pieces[py,px] == 7:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = PawnB[By,Bx]
            if Pieces[py,px] == 8:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = BishopB[By,Bx]
            if Pieces[py,px] == 9:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = KnightB[By,Bx]
            if Pieces[py,px] == 10:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = RookB[By,Bx]
            if Pieces[py,px] == 11:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = QueenB[By,Bx]
            if Pieces[py,px] == 12:
                for Bx in range(7):
                    for By in range(7):
                        Board[py*9+By+1,px*9+Bx+1] = KingB[By,Bx]

    # Pretty-ness Generator for Board
    for y in range(72):
        for x in range(72):
            if (y//9)%2 == 0:
                if (x)//9%2 == 0 and Board[y,x] != 1 and Board[y,x] != 0:
                    Board[y,x] = Brown
                elif (x)//9%2 == 1 and Board[y,x] != 1 and Board[y,x] != 0:
                    Board[y,x] = Green
            else:
                if (x)//9%2 == 0 and Board[y,x] != 1 and Board[y,x] != 0:
                    Board[y,x] = Green
                elif (x)//9%2 == 1 and Board[y,x] != 1 and Board[y,x] != 0:
                    Board[y,x] = Brown

    return Pieces, Board
