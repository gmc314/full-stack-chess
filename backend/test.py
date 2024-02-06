from script import *
from pprint import pprint

# testing placing a piece on the board
wb = Bishop("White", "1", ("b", 2))
placePiece(wb)
print(type(BOARD[6][1])==Bishop)

# testing moving piece
moveFromCurrentSquare(wb, ("a", 1))
print(BOARD[6][1]==" -- ")
print(type(BOARD[7][0])==Bishop)

########
# PAWN 
# testing placing a pawn on the board
wp = Pawn("White", "1", ("d", 2))
placePiece(wp)
print(type(BOARD[6][3])==Pawn)
print(wp.firstTurn)

# testing moving piece
moveFromCurrentSquare(wp, ("d", 4))
print(BOARD[6][3]==' -- ')
print(type(BOARD[4][3])==Pawn)
print(not wp.firstTurn)

# testing invalid move
bp = Pawn("Black", "1", ("h", 7))
placePiece(bp)
print(type(BOARD[1][7])==Pawn)
print(moveFromCurrentSquare(bp, ("h", 4)) == "invalid move")

# testing one square diagonals
print(getOneSquareDiag1(wb, wb.location)==False)
print(getOneSquareDiag2(wb, wb.location)==False)
print(getOneSquareDiag3(wb, wb.location)==False)
print(getOneSquareDiag4(wb, wb.location)==('b', 2))

# testing one square cardinals
print(getOneSquareDown(wb, wb.location)==False)
print(getOneSquareDown(wp, wp.location)==('d', 3)) 
print(getOneSquareUp(bp, bp.location)==('h', 8))
print(getOneSquareLeft(wb, wb.location)==False)
print(getOneSquareRight(wp, wp.location)==('e', 4))

# testing king valid move
wk = King("White", "4", ("c", 6))
placePiece(wk)
print(type(BOARD[2][2])==King)

print(wk.isMoveValid(("c", 5))==True)
print(wk.isMoveValid(("c", 7))==True)
print(wk.isMoveValid(("b", 6))==True)
print(wk.isMoveValid(("d", 6))==True)
print(wk.isMoveValid(("d", 7))==True)
print(wk.isMoveValid(("d", 5))==True)
print(wk.isMoveValid(("b", 7))==True)
print(wk.isMoveValid(("b", 5))==True)
print(wk.isMoveValid(("a", 5))==False)

# moving white king
print(moveFromCurrentSquare(wk, ("b", 5))=="K C6 to B5. ")
print(moveFromCurrentSquare(wk, ("d", 7))=="invalid move")
print(wk.location==("b", 5))
moveFromCurrentSquare(wk, ("b", 5))

######## 
# QUEEN
# testing queen capture
bn = Knight("Black", "8", ("b", 8))
placePiece(bn)
wq = Queen("White", "123", ("b", 6))

print(getValidMovesInStraightDir(wq, getOneSquareUp, wq.location))

print(moveFromCurrentSquare(wq, bn.location))


#########
# KNIGHT
# obstructed knight wheel
bn2 = Knight("Black", "8", ("g", 1))
placePiece(bn2)
bp2 = Pawn("Black", "8", ("e", 2))
placePiece(bp2)
print(bn2.getValidMoves())

# two pawns are placed for testing knight's ability to jump over any piece
bp2 = Pawn("Black", "8", ("f", 2))
placePiece(bp2)
wp2 = Pawn("White", "8", ("d", 2))
placePiece(wp2)

# this pawn is placed for the knight to capture
wp3 = Pawn("White", "8", ("c", 2))
placePiece(wp3)

# placing the knight and printing valid moves via knightWheel function
bn5 = Knight("Black", "8", ("e", 3))
placePiece(bn5)
print(bn5.getValidMoves())

# capturing the pawn
print(moveFromCurrentSquare(bn5, wp3.location))
print(bn5.getValidMoves())
########
# BISHOP
# capturing the knight


#######
# KING
bk = King("Black", "7", ("e", 6))
placePiece(bk)
print(bk.getValidMoves())