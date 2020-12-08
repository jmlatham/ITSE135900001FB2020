from .SailingShip import SailingShip

class BlackPearl(SailingShip):
  BlackPearlCount = 0
  def __init__(self, name, owner, sound = "Yo Ho and a bottle of rum!"):
    self.sound = sound
    BlackPearl.BlackPearlCount += 1
    super().__init__(name, owner, self.sound)