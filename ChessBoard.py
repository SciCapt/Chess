import numpy as np
from Definitions import *
from Printer import *
from Movement import *

# Generator 6 (Chess Board with peices)
def Board(Pieces, Board, t):

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

    # Develop Current Pieces Layout
    if t <= 1: # Default Layout
        # Layout of White Pieces
        Pieces[6,:] = 1
        Pieces[7,2] = 2
        Pieces[7,5] = 2
        Pieces[7,1] = 3
        Pieces[7,6] = 3
        Pieces[7,0] = 4
        Pieces[7,7] = 4
        Pieces[7,3] = 5
        Pieces[7,4] = 6
        # Layout of Black Pieces
        Pieces[1,:] = 7
        Pieces[0,2] = 8
        Pieces[0,5] = 8
        Pieces[0,1] = 9
        Pieces[0,6] = 9
        Pieces[0,0] = 10
        Pieces[0,7] = 10
        Pieces[0,3] = 11
        Pieces[0,4] = 12

        if t == 1:
            print('Example input for moving the white a2 pawn up two squares:')
            print('Input for Piece = 12, Input for move = 14')
            print('\n')

        # return Printer(Pieces, Board)

    else:
        if t > 1:
            # Initial Movement
            Pieces, Board, coords = Movement(Pieces, Board, t)

            # Print Current Board (step 1/2)
            Pieces, Board = Printer(Pieces, Board)

            # Get Current Piece Coords
            cX = coords[1]
            cY = coords[0]
            pieceToMove = coords[2]

            # Get New Piece Coords
            moved = 0
            if pieceToMove != -1:
                while moved == 0:
                    toLocation = int(input("Where to Move the Piece: "))
                    nX = 0
                    nY = 0
                    while toLocation > 0:
                        if toLocation%10 == 0:
                            toLocation = toLocation - 10
                            nX = nX + 1
                        else:
                            toLocation = toLocation - 1
                            nY = nY + 1
                    if nY > 8 or nX > 8:
                        print('Invalid Location! Try again nerd')
                    else:
                        moved = 1

            # Generate Current Pieces Layout
            Pieces[8-nY, nX-1] = Pieces[8-cY, cX-1]
            Pieces[8-cY, cX-1] = 0
            print('')

            # Print Board After Piece Move (step 2/2)
            Pieces, Board = Printer(Pieces, Board)

    # Finish
    return Printer(Pieces, Board)
