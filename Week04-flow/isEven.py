# This is a program that asks the user to enter a number
# and checks if that number is odd or even.
# Author: Sean Elliott 

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print("{} is an even number".format(number))
else:
    print("{} is an odd number". format(number))