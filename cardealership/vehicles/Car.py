from .WheeledVehicle import WheeledVehicle

class Car(WheeledVehicle):
  CarCount = 0
  def __init__(self, name, owner, sound):
    self.sound = sound
    Car.CarCount += 1
    super().__init__(name, owner, self.sound)