# Write a small program to ask for a name and age.
# When both values are entered, check if the person
# is the right age to go on an 18-30 day holiday (they
# must be over 18 and under 31). If they are, welcome
# them to the holiday, otherwise print a polite rejection
# message refusing them entry.

name = input("Enter your name: ")
age = int(input("Enter your age {}: ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday trip, {}".format(name))
else:
    print("Sorry {}, You cannot go on the holiday trip".format(name))
