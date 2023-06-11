from chess_piece import Tile
from func_utils import * 

class Pawn:
  def __init__(self, position, color):
    self.position = position
    self.color = color # b or w
    self.piece = "p"
  def get_valid_moves(self, board):
    valid_moves = []
    if self.color == 'b':
      # Check if pieces are diagonl, if so add them to valid mvoes
      piece_diag_left = board[self.position[0] + 1][self.position[1] - 1]
      piece_diag_right = board[self.position[0] + 1][self.position[1] + 1]

      if type(piece_diag_left) != Tile:
        if piece_diag_left.color != 'b':
          valid_moves.append(coords_to_move((self.position[0] + 1, self.position[1] - 1)))
      if type(piece_diag_right) != Tile:
        if piece_diag_right.color != 'b':
          valid_moves.append(coords_to_move((self.position[0] + 1, self.position[1] + 1)))
      # Check if piece ahead is blocked
      piece_ahead = board[self.position[0] + 1][self.position[1]]
      piece_ahead_2 = board[self.position[0] + 2][self.position[1]]
      if type(piece_ahead) != Tile:
        pass
      else: 
        valid_moves.append(coords_to_move((self.position[0] + 1, self.position[1])))
        # Check if piece is on 7th rank
        if self.position[0] == 1 and type(piece_ahead_2) == Tile:
          valid_moves.append(coords_to_move((self.position[0] + 2, self.position[1])))

    # Same thing again, for white
    elif self.color == 'w':
      # Check if pieces are diagonl, if so add them to valid mvoes
      piece_diag_left = board[self.position[0] - 1][self.position[1] - 1]
      piece_diag_right = board[self.position[0] - 1][self.position[1] + 1]

      if type(piece_diag_left) != Tile:
        if piece_diag_left.color != 'w':
          valid_moves.append(coords_to_move((self.position[0] - 1, self.position[1] - 1)))
      if type(piece_diag_right) != Tile:
        if piece_diag_right.color != 'w':
          valid_moves.append(coords_to_move((self.position[0] - 1, self.position[1] + 1))) 
      # Check if piece ahead is blocked
      piece_ahead = board[self.position[0] - 1][self.position[1]]
      piece_ahead_2 = board[self.position[0] - 2][self.position[1]]
      if type(piece_ahead) != Tile:
        pass
      else: 
        valid_moves.append(coords_to_move((self.position[0] - 1, self.position[1])))
        # Check if piece is on 2th rank
        if self.position[0] == 6 and type(piece_ahead_2) == Tile:
          valid_moves.append(coords_to_move((self.position[0] - 2, self.position[1])))
    return valid_moves


class Rook:
  def __init__(self, position, color):
    self.position = position
    self.color = color # b or w
    self.piece = "r"
  def get_valid_moves(self, board):
    
    if self.color == 'b':
      pass
      
class Bishop:
  def __init__(self, position, color):
    self.position = position
    self.color = color # b or w
    self.piece = "b"
  def get_valid_moves(self,board):
    
    if self.color == 'b':
      pass
      
class Knight:
  def __init__(self, position, color):
    self.position = position
    self.color = color # b or w
    self.piece = "k"
  def get_valid_moves(self, board):
    
    if self.color == 'b':
      pass
      
class Queen:
  def __init__(self, position, color):
    self.position = position
    self.color = color # b or w
    self.piece = "q"
  def get_valid_moves(self, board):
    
    if self.color == 'b':
      pass
      
class King:
  def __init__(self, position, color):
    self.position = position
    self.color = color # b or w
    self.piece = "g"
  def get_valid_moves(self, board):
    
    if self.color == 'b':
      pass
    