from .SpaceVehicle import SpaceVehicle

class SpaceXDragon(SpaceVehicle):
  SpaceXDragonCount = 0
  def __init__(self, name, owner, sound = "Cha-ching"):
    self.sound = sound
    SpaceXDragon.SpaceXDragonCount += 1
    super().__init__(name, owner, self.sound)