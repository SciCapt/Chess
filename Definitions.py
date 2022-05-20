import numpy as np

# # White Pieces                                    Black Pieces
# Pawn = np.ones((7,7))*0.75      # Point = 1       PawnB = np.ones((7,7))*0.75     # Point = 7
# Bishop = np.ones((7,7))*0.75    # Point = 2       BishopB = np.ones((7,7))*0.75   # Point = 8
# Knight = np.ones((7,7))*0.75    # Point = 3       KnightB = np.ones((7,7))*0.75   # Point = 9
# Rook = np.ones((7,7))*0.75      # Point = 4       RookB = np.ones((7,7))*0.75     # Point = 10
# Queen = np.ones((7,7))*0.75     # Point = 5       QueenB = np.ones((7,7))*0.75    # Point = 11
# King = np.ones((7,7))*0.75      # Point = 6       KingB = np.ones((7,7))*0.75     # Point = 12

# Callable Pieces
def Piece(n):
    if n == 1:
        # Pawn Definition
        Pawn = np.ones((7,7))*0.75
        Pawn[2:7,3] = 1
        Pawn[3,2] = 1
        Pawn[6,2] = 1
        Pawn[3,4] = 1
        Pawn[6,4] = 1
        return Pawn

    elif n == 2:
        # Bishop Definition
        Bishop = np.ones((7,7))*0.75
        Bishop[:,3] = 1
        Bishop[1:3,2:5] = 1
        Bishop[5:6,2] = 1
        Bishop[5:6,4] = 1
        Bishop[6,1:2] = 1
        Bishop[6,4:5] = 1
        Bishop[6,2] = 1
        Bishop[6,5] = 1
        return Bishop

    elif n == 3:
        # Knight Definition
        Knight = np.ones((7,7))*0.75
        Knight[6,1:6] = 1
        Knight[5,2:5] = 1
        Knight[4,3] = 1
        Knight[3,2:4] = 1
        Knight[2,2:6] = 1
        Knight[1,2:5] = 1
        return Knight

    elif n == 4:
        # Rook Definition
        Rook = np.ones((7,7))*0.75
        Rook[2:7,1:6] = 1
        Rook[3:6,1] = 0.75
        Rook[3:6,5] = 0.75
        Rook[1,1] = 1
        Rook[1,3] = 1
        Rook[1,5] = 1
        return Rook

    elif n == 5:
        # Queen Definition
        Queen = np.ones((7,7))*0.75
        Queen[4:6,1:6] = 1
        Queen[6,2:5] = 1
        Queen[2:4,1] = 1
        Queen[2:4,3] = 1
        Queen[2:4,5] = 1
        return Queen

    elif n == 6:
        # King Definition
        King = np.ones((7,7))*0.75
        King[4:6,1:6] = 1
        King[4:6,2] = 0.75
        King[4:6,4] = 0.75
        King[6,2:5] = 1
        King[3,2:5] = 1
        King[0:3,3] = 1
        King[1,2:5] = 1
        return King

    elif n == 7:
        # Pawn Definition
        Pawn = np.ones((7,7))*0.75
        PawnB = np.ones((7,7))*0.75
        Pawn[2:7,3] = 1
        Pawn[3,2] = 1
        Pawn[6,2] = 1
        Pawn[3,4] = 1
        Pawn[6,4] = 1
        for j in range(7): # Black Piece Definition
            for i in range(7):
                if Pawn[j,i] == 1:
                    PawnB[j,i] = 0
                else:
                    PawnB[j,i] = 0.75
        return PawnB

    elif n == 8:
        # Bishop Definition
        Bishop = np.ones((7,7))*0.75
        BishopB = np.ones((7,7))*0.75
        Bishop[:,3] = 1
        Bishop[1:3,2:5] = 1
        Bishop[5:6,2] = 1
        Bishop[5:6,4] = 1
        Bishop[6,1:2] = 1
        Bishop[6,4:5] = 1
        Bishop[6,2] = 1
        Bishop[6,5] = 1
        for j in range(7): # Black Piece Definition
            for i in range(7):
                if Bishop[j,i] == 1:
                    BishopB[j,i] = 0
                else:
                    BishopB[j,i] = 0.75
        return BishopB

    elif n == 9:
        # Knight Definition
        Knight = np.ones((7,7))*0.75
        KnightB = np.ones((7,7))*0.75
        Knight[6,1:6] = 1
        Knight[5,2:5] = 1
        Knight[4,3] = 1
        Knight[3,2:4] = 1
        Knight[2,2:6] = 1
        Knight[1,2:5] = 1
        for j in range(7): # Black Piece Definition
            for i in range(7):
                if Knight[j,i] == 1:
                    KnightB[j,i] = 0
                else:
                    KnightB[j,i] = 0.75
        return KnightB

    elif n == 10:
        # Rook Definition
        Rook = np.ones((7,7))*0.75
        RookB = np.ones((7,7))*0.75
        Rook[2:7,1:6] = 1
        Rook[3:6,1] = 0.75
        Rook[3:6,5] = 0.75
        Rook[1,1] = 1
        Rook[1,3] = 1
        Rook[1,5] = 1
        for j in range(7): # Black Piece Definition
            for i in range(7):
                if Rook[j,i] == 1:
                    RookB[j,i] = 0
                else:
                    RookB[j,i] = 0.75
        return RookB

    elif n == 11:
        # Queen Definition
        Queen = np.ones((7,7))*0.75
        QueenB = np.ones((7,7))*0.75
        Queen[4:6,1:6] = 1
        Queen[6,2:5] = 1
        Queen[2:4,1] = 1
        Queen[2:4,3] = 1
        Queen[2:4,5] = 1
        for j in range(7): # Black Piece Definition
            for i in range(7):
                if Queen[j,i] == 1:
                    QueenB[j,i] = 0
                else:
                    QueenB[j,i] = 0.75
        return QueenB

    elif n == 12:
        # King Definition
        King = np.ones((7,7))*0.75
        KingB = np.ones((7,7))*0.75
        King[4:6,1:6] = 1
        King[4:6,2] = 0.75
        King[4:6,4] = 0.75
        King[6,2:5] = 1
        King[3,2:5] = 1
        King[0:3,3] = 1
        King[1,2:5] = 1
        for j in range(7): # Black Piece Definition
            for i in range(7):
                if King[j,i] == 1:
                    KingB[j,i] = 0
                else:
                    KingB[j,i] = 0.75
        return KingB
