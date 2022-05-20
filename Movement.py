import numpy as np
from Printer import *

def Movement(Pieces, Board, t):
    done = 0
    while done == 0:
        if t%2 == 0:
            pieceToMove = int(input("White Piece to Move: "))
        else:
            pieceToMove = int(input("Black Piece to Move: "))

        # Get Current Piece Coords
        cX = 0
        cY = 0
        while pieceToMove > 0:
            if pieceToMove%10 == 0:
                pieceToMove = pieceToMove - 10
                cX = cX + 1
            else:
                pieceToMove = pieceToMove - 1
                cY = cY + 1

        # Initial Movement Stuff
        canMoveToX = []
        canMoveToY = []
        currentlyMoving = Pieces[8-cY, cX-1]
        if currentlyMoving == 0:
            print("No piece selected, try again\n")
            continue

        # Create Possible Movements
        if currentlyMoving == 1 or currentlyMoving == 7:
            canMoveToX.append(cX)
            if t%2 == 0:
                canMoveToY.append(cY+1)
            else:
                canMoveToY.append(cY-1)
            if cY == 2 or cY == 7:
                if t%2 == 0:
                    canMoveToY.append(cY+2)
                else:
                    canMoveToY.append(cY-2)

            # Coords and Such
            coords = []
            coords.append(cY)
            coords.append(cX)
            coords.append(pieceToMove)

            print('Possible Moves:')
            for jj in range(len(canMoveToY)):
                for ii in range(len(canMoveToX)):
                    print(f'{canMoveToX[ii]}{canMoveToY[jj]}')
                    # try:
                    #     Pieces[8-canMoveToY[jj],canMoveToX[ii]-1] = 0.069
                    # except:
                    #     print('were you trying to move the other person pieces??')
                    #     coords[2] = -1

        # Completion
        Pieces, Board = Printer(Pieces, Board)
        return Pieces, Board, coords
        done = 1
