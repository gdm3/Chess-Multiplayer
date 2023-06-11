import chess_utils 
from chess_utils import debug_board
from pieces import Pawn, Rook, Bishop, Knight, Queen, King

class Board:
  def __init__(self):
    # [Piece, Color] - king is 'g'
    self.board = chess_utils.create_board()
    debug_board(self.board)
    print(self.board[6][0].get_valid_moves(self.board))
  # Move should be in format (e, 2), (e, 4) etc
  # Returns True or False if the move is legal
  def validate_move(self, move_original: tuple, move_new: tuple) -> bool: 
    return True
    
    
  def make_move(self, move_original: tuple, move_new: tuple):
    pass
        