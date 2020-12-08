from .Vehicle import Vehicle

class LandVehicle(Vehicle):
  LandVehicleCount = 0
  def __init__(self, name, owner, sound = "ooga ooga"):
    self.sound = sound
    LandVehicle.LandVehicleCount += 1
    super().__init__(name, owner, self.sound)