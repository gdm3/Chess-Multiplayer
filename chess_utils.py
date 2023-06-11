from chess_piece import Tile
from pieces import Pawn, Rook, Bishop, Knight, Queen, King




def create_board():
  return [
    [Rook((0, 0), 'b'), Knight((0, 1), 'b'), Bishop((0, 2), 'b'), Queen((0, 3), 'b'), King((0, 4), 'b'), Bishop((0, 5), 'b'), Knight((0, 6), 'b'), Rook((0, 7), 'b')],
    [Pawn((1, 0), 'b'), Pawn((1, 1), 'b'), Pawn((1, 2), 'b'), Pawn((1, 3), 'b'), Pawn((1, 4), 'b'), Pawn((1, 5), 'b'), Pawn((1, 6), 'b'), Pawn((1, 7), 'b')],
    [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
    [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
    [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
    [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
    [Pawn((6, 0), 'b'), Pawn((6, 1), 'w'), Pawn((6, 2), 'w'), Pawn((6, 3), 'w'), Pawn((6, 4), 'w'), Pawn((6, 5), 'w'), Pawn((6, 6), 'w'), Pawn((6, 7), 'w')],
    [Rook((7, 0), 'w'), Knight((7, 1), 'w'), Bishop((7, 2), 'w'), Queen((7, 3), 'w'), King((7, 4), 'w'), Bishop((7, 5), 'w'), Knight((7, 6), 'w'), Rook((7, 7), 'w')]
  ]

# Print the board to console
def debug_board(board):
  for row in board:
    print('') # Newline
    for tile in row:
      if type(tile) == Tile:
        print("_", end='')
      else:
        print(tile.piece, end='')
  print('')