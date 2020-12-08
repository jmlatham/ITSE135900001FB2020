from .Vehicle import Vehicle

class SeaVehicle(Vehicle):
  SeaVehicleCount = 0
  def __init__(self, name, owner, sound="Splash Splash"):
    self.sound = sound
    SeaVehicle.SeaVehicleCount += 1
    super().__init__(name, owner, self.sound)