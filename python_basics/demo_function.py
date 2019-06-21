# Function with required parameters
def hello_1(name):
   print("My name is ", name)

hello_1("Sharat")


# Function with optional paramaters
def hello_2(name="everyone"):
   """ Greet a person!"""
   print("Hello ", name)
   print("The docstring is " + hello_2.__doc__)

hello_2()


# Arbitrary number of parameters
def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """

    return (first + sum(values)) / (1 + len(values))

print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))


# Arbitrary Number of Keyword Parameters
def f(**kwargs):
    print(kwargs)

f(de="German",en="English",fr="French")
