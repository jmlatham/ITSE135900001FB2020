def displayDictionaryMenu(menuDictionary, title="MENU"):
  printMenuTitle(title)
  for key in menuDictionary:
    print("\t", end="")
    print(key, menuDictionary[key], sep=". ")
  printStars()

def getMenuChoice(inputMessage="Please select a menu option: "):
  return input(inputMessage)

def printMenuTitle(title="MENU"):
  menuTitle = "*** " + title + " ***"
  print()
  printStars(len(menuTitle))
  print(menuTitle)
  printStars(len(menuTitle))

def printStars(number=13):
  print("*" * number)

def displayNestedMenu(menuDictionary, title=""):
  printMenuTitle(title)
  for key in menuDictionary:
    print("\t", end="")
    print(key, menuDictionary[key]["name"], sep=". ")
  printStars()