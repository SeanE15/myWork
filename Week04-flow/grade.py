# This is a program that reads in a students percentage and 
# prints out the correct grade
# Author: Sean Elliott

percentage = float(input("Enter the percentage: "))

if percentage <0 or percentage > 100 :
    print ("Please enter a number between 0 and 100: ")
elif percentage < 40: 
    print ("Fail") 
elif percentage < 50:
    print ("Pass") 
elif percentage < 60:
    print ("Merit 2")
elif percentage < 70: 
    print ("Merit 1") 
else: 
    print ("Distinction") 