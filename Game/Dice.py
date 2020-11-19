import random
class Dice:
  __sides__ = 6

  def __init__(self, sides=6):
    self.__sides__ = sides
  
  def roll(self):
    rollResult = random.randint(1,self.__sides__)
    return rollResult