class Vehicle:
  __VehicleCount = 0
  serialNumber = ""
  keyLocation = ""
  name = ""
  owner = ""
  def __init__(self, name="VEHICLE", owner="AVAILABLE", sound="hiyucka hiyucka", color="white"):
    self.sound = sound
    self.primaryColor = color
    Vehicle.__VehicleCount += 1
    self.name = name
    self.owner = owner

  def blowHorn(self):
    print(self.sound)

  def setSecondaryColor(self, color):
    self.secondaryColor = color
  
  def __str__(self):
    return "{} owns {}.".format(self.owner,self.name)