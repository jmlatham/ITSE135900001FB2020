from .HelperFunctions import displayDictionaryMenu, getMenuChoice, displayNestedMenu
import json
from .vehicles.Vehicle import Vehicle
from .vehicles.LandVehicle import LandVehicle
from .vehicles.SeaVehicle import SeaVehicle
from .vehicles.AirVehicle import AirVehicle
from .vehicles.SpaceVehicle import SpaceVehicle
from .vehicles.WheeledVehicle import WheeledVehicle
from .vehicles.TrackedVehicle import TrackedVehicle
from .vehicles.HoverCraftVehicle import HoverCraftVehicle
from .vehicles.Car import Car
from .vehicles.Truck import Truck
from .vehicles.BlackPearl import BlackPearl
from .vehicles.SailingShip import SailingShip
from .vehicles.SpaceShuttle import SpaceShuttle
from .vehicles.SpaceXDragon import SpaceXDragon
from .vehicles.SSMinow import SSMinow
from .vehicles.Submarine import Submarine
from .vehicles.TieFighter import TieFighter
from .vehicles.XWingFighter import XWingFighter

class Inventory:
  __filesPath = "files/"
  menu = {"0":"Quit Inventory","1":"Add Vehicle","2":"Add Vehicles from file","3":"delete vehicle","4":"list vehicles"}
  vehicleMenu={
    "Vehicle":{
      "1":{"name":"AirVehicle","menu":{}},
      "2":{"name":"LandVehicle","menu":
        {
          "1":{"name":"Tracked Vehicles"},
          "2":{"name":"Wheeled Vehicles"}}},
      "3":{"name":"SeaVehicle","menu":{}},
      "4":{"name":"SpaceVehicle","menu":{}}
    }
  }
  vehicleList = []
  def __init__(self):
    pass

  def displayMenu(self):
    while True:
      displayDictionaryMenu(self.menu, title="Inventory")
      menuChoice = getMenuChoice()
      if menuChoice == "1":
        self.addVehicle(None)

      elif menuChoice == "2":
        self.addVehicleFromDataStore()

      elif menuChoice == "3":
        self.delVehicle(None)
      elif menuChoice == "4":
        self.listVehicles()
      else:
        break
        
  def displayVehicleMenu(self, vehicleMenu):
    displayNestedMenu(vehicleMenu, title="Vehicle Menu")
    menuChoice = getMenuChoice()
    return menuChoice
    

  def addVehicle(self, vehicle):
    if self.displayVehicleMenu(self.vehicleMenu["Vehicle"]) == "1":
      pass
    print("Add Vehicle")
    print(vehicle)
    print("\n" * 3)
  
  def addVehicleFromDataStore(self, file_name="vehicles.json"):
    print("Add from file")
    self.loadVehicles(file_name)
    print("\n" * 3)
  
  def delVehicle(self, vehicle):
    print("Delete Vehicle")
    print(vehicle)
    print("\n" * 3)
  
  def listVehicles(self):
    print("Vehicles List:")
    if len(self.vehicleList) < 1:
      self.loadVehicles()
    print(self.vehicleList)
    print("\n" * 3)

  def loadVehicles(self, file_name):
    vehicleDictionary = ""
    with open(self.__filesPath + file_name, "r") as f:
      vehicleDictionary = json.load(f)
    print(vehicleDictionary.keys())
    # create the objects
    for key in vehicleDictionary.keys():
      
      print("*"*5)
      if vehicleDictionary[key]["Type"] == "Vehicle":
        vehicle = Vehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " Vehicle")
        print(self.vehicleList)
      elif vehicleDictionary[key]["Type"] == "LandVehicle":
        vehicle = LandVehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " LandVehicle")
      elif vehicleDictionary[key]["Type"] == "AirVehicle":
        vehicle = AirVehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " AirVehicle")
      elif vehicleDictionary[key]["Type"] == "SpaceVehicle":
        vehicle = SpaceVehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " SpaceVehicle")
      elif vehicleDictionary[key]["Type"] == "SeaVehicle":
        vehicle = SeaVehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " SeaVehicle")
      elif vehicleDictionary[key]["Type"] == "BlackPearl":
        vehicle = BlackPearl(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " BlackPearl")
      elif vehicleDictionary[key]["Type"] == "Car":
        vehicle = Car(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"], sound="beep")
        self.vehicleList.append(vehicle)
        print(vehicle, " Car")
      elif vehicleDictionary[key]["Type"] == "HoverCraftVehicle":
        vehicle = HoverCraftVehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " HoverCraftVehicle")
      elif vehicleDictionary[key]["Type"] == "SailingShip":
        vehicle = SailingShip(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " SailingShip")
      elif vehicleDictionary[key]["Type"] == "SpaceShuttle":
        vehicle = SpaceShuttle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " SpaceShuttle")
      elif vehicleDictionary[key]["Type"] == "SpaceXDragon":
        vehicle = SpaceXDragon(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " SpaceXDragon")
      elif vehicleDictionary[key]["Type"] == "SSMinow":
        vehicle = SSMinow(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " SSMinow")
      elif vehicleDictionary[key]["Type"] == "Submarine":
        vehicle = Submarine(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " Submarine")
      elif vehicleDictionary[key]["Type"] == "TieFighter":
        vehicle = TieFighter(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " TieFighter")
      elif vehicleDictionary[key]["Type"] == "TrackedVehicle":
        vehicle = TrackedVehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " TrackedVehicle")
      elif vehicleDictionary[key]["Type"] == "Truck":
        vehicle = Truck(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"], sound="honk honk")
        self.vehicleList.append(vehicle)
        print(vehicle, " Truck")
      elif vehicleDictionary[key]["Type"] == "WheeledVehicle":
        vehicle = WheeledVehicle(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " WheeledVehicle")
      elif vehicleDictionary[key]["Type"] == "XWingFighter":
        vehicle = XWingFighter(name=vehicleDictionary[key]["Name"], owner=vehicleDictionary[key]["Owner"])
        self.vehicleList.append(vehicle)
        print(vehicle, " XWingFighter")
      else:
        print("Type:", vehicleDictionary[key]["Type"])
        print("Name:", vehicleDictionary[key]["Name"])
        print("Owner:", vehicleDictionary[key]["Owner"])
        # print(self.vehicleList)
    # put the objects into the list
    