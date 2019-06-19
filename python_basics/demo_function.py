# Function with required parameters
def hello_1(name):
   print("My name is ", name)

# Function with optional paramaters
def hello_2(name="everyone"):
   """ Greet a person!"""
   print("Hello ", name)
   print("The docstring is " + hello_2.__doc__)


