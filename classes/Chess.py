class ChessGame:
  __blackCapturedPieces__ = []
  __whiteCapturedPieces__ = []
  __blackPieces__ = []
  __whitePieces__ = []

  def __init__(self):
    pass

  def __buildBoard__(self):
    pass
  
  def startGame(self):
    pass
  
  def stopGame(self):
    pass
  
  def movePiece(self):
    pass
  
  def capturePiece(self):
    pass
  
  def checkMovement(self):
    pass
  
  def displayBoard(self):
    pass

  def displayMenu(self, menuToDisplay):
    pass

  
class GamePiece:
  __name__ = ""
  __column__ = None
  __row__ = None

  def __init__(self, name=""):
    self.__name__ = name

  def setName(self, name):
    pass
  
  def getName(self):
    return self.__name__

  def setPosition(self, column, row):
    self.__column__ = column
    self.__row__ = row

  def getPosition(self):
    return {"column":self.__column__, "row":self.__row__}

class Rook(GamePiece):
  pass

class Knight(GamePiece):
  pass

class Bishop(GamePiece):
  pass

class Queen(GamePiece):
  pass

class King(GamePiece):
  pass

class Pawn(GamePiece):
  pass