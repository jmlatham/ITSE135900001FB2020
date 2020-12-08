from .WheeledVehicle import WheeledVehicle

class Truck(WheeledVehicle):
  TruckCount = 0
  def __init__(self, name, owner, sound):
    self.sound = sound
    Truck.TruckCount += 1
    super().__init__(name, owner, self.sound)