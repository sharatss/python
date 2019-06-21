def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = input("Input the value of n: ")
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of {} is {}".format(n, factorial(n)))
