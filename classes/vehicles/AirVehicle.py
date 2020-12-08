from .Vehicle import Vehicle

class AirVehicle(Vehicle):
  AirVehicleCount = 0
  def __init__(self, name="UNKNOWN", owner="AVAILABLE", sound = "swoosh"):
    self.sound = sound
    AirVehicle.AirVehicleCount += 1
    super().__init__(name, owner, self.sound)