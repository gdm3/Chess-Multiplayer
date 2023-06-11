class Tile:
  def __init__(self, piece=None, color=None):
    if piece:
      self.is_blank = False
    else:
      self.is_blank = True
    self.piece = piece
    self.color = color