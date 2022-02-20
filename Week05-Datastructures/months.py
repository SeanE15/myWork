# A tuple that stores the months of the year, from that tuple create 
# another tuple with just the summer months (May, June, July), print out the 
# summer months one at a time.

#Author: Sean Elliott 


months = ("Janurary",    
            "February", 
            "March", 
            "April", 
            "May", 
            "June", 
            "July", 
            "August",
            "September",
            "October", 
            "November",
            "December"
            )

summer = months[4:7]
for month in summer: 
    print(month) 