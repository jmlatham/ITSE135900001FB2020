from .SpaceVehicle import SpaceVehicle

class SpaceShuttle(SpaceVehicle):
  SpaceShuttleCount = 0
  def __init__(self, name, owner, sound = "boom"):
    self.sound = sound
    SpaceShuttle.SpaceShuttleCount += 1
    super().__init__(name, owner, self.sound)