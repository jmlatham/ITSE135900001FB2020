from .SpaceVehicle import SpaceVehicle

class TieFighter(SpaceVehicle):
  TieFighterCount = 0
  def __init__(self, name, owner, sound = "pew pew"):
    self.sound = sound
    TieFighter.TieFighterCount += 1
    super().__init__(name, owner, self.sound)