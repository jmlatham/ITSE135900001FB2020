from classes.ExampleClass import ExampleClass

eClass = ExampleClass("me", 13)
print("My First Program in Python!!")

print("\n""private values:")
print(eClass.getPrivateVariable1())
print(eClass.getPrivateVariable2())

print("\n""public values:")
print(eClass.name, eClass.age)

print()
print("Added GitHub")