from .LandVehicle import LandVehicle

class TrackedVehicle(LandVehicle):
  TrackedVehicleCount = 0
  def __init__(self, name, owner, sound = "grrrrr"):
    self.sound = sound
    TrackedVehicle.TrackedVehicleCount += 1
    super().__init__(name, owner, self.sound)