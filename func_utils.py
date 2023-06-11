from chess_utils import Tile
mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
mapping_rev = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7:'h'}
mapping_nums = {}
def move_to_coords(move: tuple) -> tuple:
  return (7 - (move[1] - 1), mapping[move[0]])

def coords_to_tile(coords: tuple, board) -> Tile:
  return board[coords[0]][coords[1]]

def coords_to_move(coords: tuple) -> tuple:
  move_letter = mapping_rev[coords[1]]
  move_number = abs(8 - coords[0])
  return (move_letter, move_number)