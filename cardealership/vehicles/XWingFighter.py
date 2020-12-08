from .SpaceVehicle import SpaceVehicle

class XWingFighter(SpaceVehicle):
  XWingFighterCount = 0
  def __init__(self, name, owner, sound = "zap zap"):
    self.sound = sound
    XWingFighter.XWingFighterCount += 1
    super().__init__(name, owner, self.sound)