from classes.ExampleClass import ExampleClass

exampleClass = ExampleClass("Marshall", 3)
print(exampleClass.name)
exampleClass.age = 103
exampleClass.name = "John"
print(exampleClass.name, exampleClass.age)

print(exampleClass.privateVariable1)
print(exampleClass.__privateVariable1)




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