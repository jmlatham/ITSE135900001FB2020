from .LandVehicle import LandVehicle

class WheeledVehicle(LandVehicle):
  WheeledVehicleCount = 0
  def __init__(self, name, owner, sound = "urt urt"):
    self.sound = sound
    WheeledVehicle.WheeledVehicleCount += 1
    super().__init__(name, owner, self.sound)