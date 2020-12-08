from .SeaVehicle import SeaVehicle

class Submarine(SeaVehicle):
  SubmarineCount = 0
  def __init__(self, name, owner, sound = "ping... ping..."):
    self.sound = sound
    Submarine.SubmarineCount += 1
    super().__init__(name, owner, self.sound)