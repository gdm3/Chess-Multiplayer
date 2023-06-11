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
        try:
          if piece_diag_left.color != 'b':
            valid_moves.append(coords_to_move((self.position[0] + 1, self.position[1] - 1)))
        except KeyError: # On the edge of the board
          print('Piece is on the left edge of the board')
      if type(piece_diag_right) != Tile:
        try:
          if piece_diag_right.color != 'b':
            valid_moves.append(coords_to_move((self.position[0] + 1, self.position[1] + 1)))
        except KeyError: # On the edge of the board
          print('Piece is on the right edge of the board')
      # Check if piece ahead is blocked
      piece_ahead = board[self.position[0] + 1][self.position[1]]
      try:
        piece_ahead_2 = board[self.position[0] + 2][self.position[1]]
      except IndexError: # On the edge of the board
        print('Piece is on the edge of the board vertically') 
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
        try:
          if piece_diag_left.color != 'w':
            valid_moves.append(coords_to_move((self.position[0] - 1, self.position[1] - 1)))
        except KeyError: # On the edge of the board
          print('Piece is on the left edge of the board')
      if type(piece_diag_right) != Tile:
        try:
          if piece_diag_right.color != 'w':
            valid_moves.append(coords_to_move((self.position[0] - 1, self.position[1] + 1))) 
        except KeyError: # On the edge of the board
          print('Piece is on the right edge of the board')
      # Check if piece ahead is blocked
      piece_ahead = board[self.position[0] - 1][self.position[1]]
      try:
        piece_ahead_2 = board[self.position[0] - 2][self.position[1]]
      except IndexError: # On the edge of the board
        print('Piece is on the edge of the board vertically')
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
    valid_moves = []
    if self.color == 'b':
      # Loop thtrough tiles vertically, up first
      if self.position[0] != 0:
        for i in range(self.position[0] - 1, 0, -1):
          # If tile is empty, add it to valid moves
          if type(board[i][self.position[1]]) == Tile:
            valid_moves.append(coords_to_move((i, self.position[1])))
          # Else, check if tile is occupied by a piece of the opposite color and break
          elif board[i][self.position[1]].color == 'w':
            valid_moves.append(coords_to_move((i, self.position[1])))
            break
      
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
    