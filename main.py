from classes.ExampleClass import ExampleClass
from Labs import Labs






if False:
  anything = input("Enter a number: ")
  something = anything * 2.0
  print(anything, "to the power of 2 is", something)

  userAge = int(input("Enter Your Age: "))
  userName = input("Enter Your Name: ")
  favoriteAge = 54

  category1CutOff = 18
  category2CutOff = 13

  if userAge >= category1CutOff:
    print("Hello, ", userName)
    print("Welcome to our program at Category 1. You are our priority!")
    if (userName.lower() == "smith" or userName.lower() == "bill") and userAge==favoriteAge:
      print("you are my favorite person.")
  elif userAge >= category2CutOff:
    print("Yo!", userName)
    print("You are in Category 2. ")
    if userName.lower() == "jones":
      print("you are my favorite person.")
  elif userAge >= 3:
    print("hi little camper")
    print("you are ", userAge, "years old")
  else:
    print("Get out of here, you are not old enough.")




if False:
  var = 1
  account_balance = 1000.0
  client_name = 'John Doe'
  print(var, account_balance, client_name)


if False:
  print(True > False)
  print(True < False)
  AgeOfCat = input("What is the age of your cat?")
  if AgeOfCat == 0:
    print("Sorry can't commute")
  else:
    print(1/AgeOfCat)



if False:
  print("helloooooo,","nurse!!!", sep=" ", end="\n")
  print('Yako said, "Hello, nurse"')
  print("No he didn't!")
  print('No he didn\'t')
  print("H", "E", "L" "L", "O", sep="-")


  print(123)
  print('c')

  print(11111111)
  print(11,111,111)
  print(11_111_111)
  print("11,111,111")

  variable1 = 11111111
  variable2 = "11111111"
  print(variable1)
  print(variable2)
  print(variable1*3)
  print(variable2*3)
  print(variable1*variable2)

if False:
  module2 = Labs()
  module2.runLab2_1_1_7()



if False:
  exampleClass = ExampleClass("Marshall", 3)
  print(exampleClass.doubleMyAge())
  print(exampleClass.name)
  exampleClass.age = 103
  exampleClass.name = "John"
  print(exampleClass.name, exampleClass.age)

  #print(exampleClass.privateVariable1)
  #print(exampleClass.__privateVariable1)

if False:
  eClass = ExampleClass("me", 13)
  print("My First Program in Python!!")
  print(eClass.doubleMyAge())
  print("\n""private values:")
  print(eClass.getPrivateVariable1())
  eClass.setPrivateVariable1("private Variable 1 has changed")



  print(eClass.getPrivateVariable1())
  print("\nnow working with \"#2\"\n")
  print(eClass.getPrivateVariable2())


  eClass.setPrivateVariable2("abc")
  print(eClass.getPrivateVariable2())
  eClass.setPrivateVariable2("def")
  print(eClass.getPrivateVariable2())
  
  flamawhammer = ExampleClass("",15)
  print("------------")
  print(flamawhammer.doubleMyAge())
  

  print("\n""public values:")
  print(eClass.name, eClass.age)

  print()
  print("Added GitHub")



























if False:
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
  print(issubclass(Car, Vehicle))
  print(issubclass(WheeledVehicle, SpaceVehicle))