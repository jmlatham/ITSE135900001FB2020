import random, json
from os import strerror

class JSONVehicles:
  __filesPath = "files/"
  __VEHICLE_TYPES = ["AirVehicle","BlackPearl","Car","HoverCraftVehicle","LandVehicle","SailingShip","SeaVehicle","SpaceShuttle","SpaceVehicle","SpaceXDragon","SSMinow","Submarine","TieFighter","TrackedVehicle","Truck","Vehicle","WheeledVehicle","XWingFighter"]
  __VEHICLE_NAMES = ["ASTON MARTIN","AUDI","BENTLEY","BMW","BUGATTI","DAIMLERCHRYSLER","FERRARI","FORD","MUSTANG","FUJI","GM","CORVETTE","HONDA","HYUNDAI","JAGUAR","KIA","LAMBORGHINI","LAND ROVER","LOTUS","MASERATI","MAZDA","MERCEDES BENZ","MITSUBISHI","NUMMI","NISSAN","PORSCHE","ROLLS-ROYCE","ROUSH","SPYKER","SUZUKI","TOYOTA","VOLKSWAGEN","VOLVO"]
  __OWNERNAMES = ["Brayden", "Ellioth","Ethan", "Gabe", "Josh", "Kane", "Mike", "Miguel","Ravi","Taylor","Amy","Keylin"]
  def __init__(self):
    pass

  def buildString(self, VehicleType, VehicleName, Owner):
    pass

  def getRandomInt(self, max):
    return random.randint(0,max-1)

  def createDictionary(self, record_count):
    vehicles = {}
    for vehicleId in range(record_count):
      vehicleType = JSONVehicles.__VEHICLE_TYPES[self.getRandomInt(len(JSONVehicles.__VEHICLE_TYPES))]
      vehicleName = JSONVehicles.__VEHICLE_NAMES[self.getRandomInt(len(JSONVehicles.__VEHICLE_NAMES))]
      vehicleOwner = JSONVehicles.__OWNERNAMES[self.getRandomInt(len(JSONVehicles.__OWNERNAMES))]
      vehicles[vehicleId] = {"Type":vehicleType,"Name":vehicleName,"Owner":vehicleOwner}
    return vehicles
  
  def createFile(self, file_name="json_file.json", record_count=100):
    if record_count > 0:
      vehicles = self.createDictionary(record_count)
      # vehicles = vehicles.replace('"}, "','"},\n"')
      vehiclesString = json.dumps(vehicles).replace('"}, "','"},\n"')
      try:
        with open(self.__filesPath+file_name, 'w') as f:
          # json.dump(vehicles, f)
          f.write(vehiclesString)
        print("Your file was created.\n")
      except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))
    else: 
      print("\nNo file was created because you entered a value less than 1.\n")
  
  def createVehiclesFile(self):
    try:
      self.createFile("vehicles.json", int(input("How many records do you want? ")))
    except:
      print("You need to enter an integer to continue")
      self.createVehiclesFile()
    
  
  def readFile(self, file_name="json_file.json"):
    try:
      with open(self.__filesPath+file_name,'r') as f:
        print(json.dumps(json.load(f),indent=4))
    except IOError as e:
      print("I/O error occurred: ", strerror(e.errno))


      