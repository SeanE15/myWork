

import sys

file = open(mobydick.txt, "r") 

print(file, sys.argv[0])

print ("Number of occurences of the letter e in the file:", len(sys.argv))

#I start by asking the program to open the file, and open it in the read format only. This is denoted by the 'r'.

# I ask the program to read the entire text file - note that we have not asked it to output the file - only scan it for the information that we require.

# I have now asked the program to perform the count function which will count the entire txt doc and calculate the number of letters designated by the below line of code. Please note that the 'e' is in fact case sensitive
# (like everything else in Python) and as such it is not counting capital E's.
