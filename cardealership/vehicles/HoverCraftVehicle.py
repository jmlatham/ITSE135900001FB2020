from .LandVehicle import LandVehicle

class HoverCraftVehicle(LandVehicle):
  HoverCraftVehicleCount = 0
  def __init__(self, name, owner, sound = "SHHSHSHHHSHSHSHHSH"):
    self.sound = sound
    HoverCraftVehicle.HoverCraftVehicleCount +=0
    super().__init__(name, owner, self.sound)