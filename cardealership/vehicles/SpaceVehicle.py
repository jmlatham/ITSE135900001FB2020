from .Vehicle import Vehicle

class SpaceVehicle(Vehicle):
  SpaceVehicleCount = 0
  def __init__(self, name, owner, sound = "<<< Total Silence >>>"):
    self.sound = sound
    SpaceVehicle.SpaceVehicleCount += 1
    super().__init__(name, owner, self.sound)