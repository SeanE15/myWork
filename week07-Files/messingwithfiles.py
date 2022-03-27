# Write a program that counts how many times it was run.
# Author: Sean Elliott 

fileName = "count.txt"
def readNumber(): 
   with open(fileName) as f: 
        number = int(f.read())
        return number 

#num = readNumber ()
#print (num) 

#fileName = "count.txt"
#def writeNumber(number):
    #with open (fileName, "wt") as f: 
        #f.write(str(number))

#writeNumber(3) 

def writeNumber(number): 
    with open(fileName, "wt") as f: 
        f.write(str(number))

num = readNumber()
num += 1
print ("We ahve run this program {} times".format(num))
writeNumber(num) 