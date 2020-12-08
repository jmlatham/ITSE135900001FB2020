from .SeaVehicle import SeaVehicle

class SSMinow(SeaVehicle):
  SSMinowCount = 0
  def __init__(self, name, owner, sound = "Gilligan!"):
    self.sound = sound
    SSMinow.SSMinowCount += 1
    super().__init__(name, owner, self.sound)