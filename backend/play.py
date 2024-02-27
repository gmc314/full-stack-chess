from pprint import pprint
from script import *

def newGame():
    clearBoard()
    # get new instances of all pieces
    bk = King("Black", "1", ('e', 8))
    placePiece(bk)
    bq = Queen("Black", "2", ('d', 8))
    placePiece(bq)
    bb1 = Bishop("Black", "3", ('c', 8))
    placePiece(bb1)
    bb2 = Bishop("Black", "4", ('f', 8))
    placePiece(bb2)
    bn1 = Knight("Black", "5", ('b', 8))
    placePiece(bn1)
    bn2 = Knight("Black", "6", ('g', 8))
    placePiece(bn2)
    br1 = Rook("Black", "7", ('a', 8))
    placePiece(br1)
    br2 = Rook("Black", "8", ('h', 8))
    placePiece(br2)
    bp1 = Pawn("Black", "9", ('a', 7))
    placePiece(bp1)
    bp2 = Pawn("Black", "10", ('b', 7))
    placePiece(bp2)
    bp3 = Pawn("Black", "11", ('c', 7))
    placePiece(bp3)
    bp4 = Pawn("Black", "12", ('d', 7))
    placePiece(bp4)
    bp5 = Pawn("Black", "13", ('e', 7))
    placePiece(bp5)
    bp6 = Pawn("Black", "14", ('f', 7))
    placePiece(bp6)
    bp7 = Pawn("Black", "15", ('g', 7))
    placePiece(bp7)
    bp8 = Pawn("Black", "16", ('h', 7))
    placePiece(bp8)

    wk = King("White", "17", ('e', 1))
    placePiece(wk)
    wq = Queen("Black", "18", ('d', 1))
    placePiece(wq)
    wb1 = Bishop("Black", "19", ('c', 1))
    placePiece(wb1)
    wb2 = Bishop("Black", "20", ('f', 1))
    placePiece(wb2)
    wn1 = Knight("Black", "21", ('b', 1))
    placePiece(wn1)
    wn2 = Knight("Black", "22", ('g', 1))
    placePiece(wn2)
    wr1 = Rook("Black", "23", ('a', 1))
    placePiece(wr1)
    wr2 = Rook("Black", "24", ('h', 1))
    placePiece(wr2)
    wp1 = Pawn("Black", "25", ('a', 2))
    placePiece(wp1)
    wp2 = Pawn("Black", "26", ('b', 2))
    placePiece(wp2)
    wp3 = Pawn("Black", "27", ('c', 2))
    placePiece(wp3)
    wp4 = Pawn("Black", "28", ('d', 2))
    placePiece(wp4)
    wp5 = Pawn("Black", "29", ('e', 2))
    placePiece(wp5)
    wp6 = Pawn("Black", "30", ('f', 2))
    placePiece(wp6)
    wp7 = Pawn("Black", "31", ('g', 2))
    placePiece(wp7)
    wp8 = Pawn("Black", "32", ('h', 2))
    placePiece(wp8)
    return "Board ready"


# plan for the main playGame function
def playGame():
    newGame()
    whiteKing = [piece for piece in WHITE.pieces if isinstance(piece, King)][0]
    blackKing = [piece for piece in BLACK.pieces if isinstance(piece, King)][0]
    whiteCheckmate = False
    blackCheckmate = False
    while not whiteCheckmate or not blackCheckmate:
        whitemove = input("White's Move: ")
        moveFromCurrentSquare(**whitemove)
        # define a move function where the input is converted to a square and a piece
        blackCheckmate = checkmate(blackKing)

        blackmove = input("Black's Move: ")
        moveFromCurrentSquare(**blackmove)
        # define a move function where the input is converted to a square and a piece
        whiteCheckmate = checkmate(whiteKing)

pprint(BOARD)