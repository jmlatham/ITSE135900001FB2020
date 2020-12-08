class ExampleClass:
  __privateVariable1 = "private variable A"
  __privateVariable2 = "private variable B"

  def __init__(self, nameValue="Jones", ageValue=13):
    self.name = nameValue
    self.age = ageValue

  def setPrivateVariable1(self, value):
    self.__privateVariable1 = value

  def setPrivateVariable2(self, value):
    self.__privateVariable2 = self.__privateVariable2 + value

  def getPrivateVariable1(self):
    if(self.name=="Kyle"):
      return "sorry sucker"
    else:
      return self.__privateVariable1
    #return self.name
  
  def getPrivateVariable2(self):
    return self.__privateVariable2

  def doubleMyAge(self):
    return int(self.age)*2


if __name__ == "__main__":
  myClass1 = ExampleClass()
  myClass2 = ExampleClass("Smith")
  myClass3 = ExampleClass("Lee", 45)
  myClass1.getPrivateVariable1()