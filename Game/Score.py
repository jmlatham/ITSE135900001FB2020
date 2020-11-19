class Score:
  __total__ = 0
  def __init__(self):
    pass

  def addPoints(self, points):
    self.__total__ += points

  def subtractPoints(self, points):
    self.__total__ -= points

  def getScore(self):
    return self.__total__

  def checkRoll(self, diceContainer):
    pass

  def getScorePossibilities(self):
    pass