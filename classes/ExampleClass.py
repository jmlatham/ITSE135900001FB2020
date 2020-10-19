class ExampleClass:
  __privateVariable1 = "private variable A"
  __privateVariable2 = "private variable B"

  def __init__(self, nameValue, ageValue):
    self.name = nameValue
    self.age = ageValue
  
  def setPrivateVariable1(self, value):
    self.__privateVariable1 = value

  def setPrivateVariable2(self, value):
    self.__privateVariable2 = value

  def getPrivateVariable1(self):
    return self.__privateVariable1
  
  def getPrivateVariable2(self):
    return self.__privateVariable2