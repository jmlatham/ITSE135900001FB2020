from classes.ExampleClass import ExampleClass

exampleClass = ExampleClass("Marshall", 3)
print(exampleClass.name)
exampleClass.age = 103
exampleClass.name = "John"
print(exampleClass.name, exampleClass.age)

#print(exampleClass.privateVariable1)
#print(exampleClass.__privateVariable1)

if False:
  eClass = ExampleClass("me", 13)
  print("My First Program in Python!!")

  print("\n""private values:")
  print(eClass.getPrivateVariable1())
  print(eClass.getPrivateVariable2())

  print("\n""public values:")
  print(eClass.name, eClass.age)

  print()
  print("Added GitHub")


if True:
  from vehicles.Vehicle import Vehicle
  from vehicles.LandVehicle import LandVehicle
  from vehicles.SeaVehicle import SeaVehicle
  from vehicles.AirVehicle import AirVehicle
  from vehicles.SpaceVehicle import SpaceVehicle
  from vehicles.WheeledVehicle import WheeledVehicle
  from vehicles.TrackedVehicle import TrackedVehicle
  from vehicles.HoverCraftVehicle import HoverCraftVehicle
  from vehicles.Car import Car
  from vehicles.Truck import Truck

  vehicle = Vehicle()
  landVehicle = LandVehicle()
  seaV = SeaVehicle()
  airV = AirVehicle()
  spaceV = SpaceVehicle()
  wheeledVechicle = WheeledVehicle()
  trackedV = TrackedVehicle()
  hcV = HoverCraftVehicle()
  car1 = Car("honk honk")
  car2 = Car("beep beep")
  truck1 = Truck("hooey hooey")

  vehicle.blowHorn()
  landVehicle.blowHorn()
  wheeledVechicle.blowHorn()
  seaV.blowHorn()
  airV.blowHorn()
  spaceV.blowHorn()
  trackedV.blowHorn()
  hcV.blowHorn()
  car1.blowHorn()
  car2.blowHorn()
  truck1.blowHorn()

  print(isinstance(car1, Vehicle))
  print(isinstance(car1, SeaVehicle))