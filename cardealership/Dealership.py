from .Inventory import Inventory
from .HelperFunctions import displayDictionaryMenu, getMenuChoice

class Dealership:
  menu = {"0":"Quit Program","1":"Do Inventory","2":"runTest"}

  def __init__(self):
    pass
  def displayMenu(self, menuType):
    if menuType == "dealership":
      while True:
        displayDictionaryMenu(self.menu, title="Dealership")
        menuChoice = getMenuChoice()
        if menuChoice == "1":
          invent = Inventory() 
          invent.displayMenu()

        elif menuChoice == "2":
          self.runTest()

        else:
          break
  def runTest(self):
    print("to do list")
    print("""
sell vehicles
buy vehicles
  from manufacturers
  from auctions
Keep inventory
  Keep serial numbers
  Track Keys
    """)