from .SeaVehicle import SeaVehicle

class SailingShip(SeaVehicle):
  SailingShipCount = 0
  def __init__(self, name, owner, sound = "flap flap << of the flag and sails >>"):
    self.sound = sound
    SailingShip.SailingShipCount += 1
    super().__init__(name, owner, sound)