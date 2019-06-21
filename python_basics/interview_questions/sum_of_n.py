"""
Write a recursive Python function that returns the sum of the first n integers.
"""

def sum_of_n(n):
    if n == 0:
        return 0
    else:
        return sum_of_n(n-1) + n

n = input("Enter the value of n: ")
print(sum_of_n(n))
