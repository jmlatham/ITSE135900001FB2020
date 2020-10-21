from .WheeledVehicle import WheeledVehicle

class Car(WheeledVehicle):
  def __init__(self, sound):
    self.sound = sound