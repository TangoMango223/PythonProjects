#Python - 6 sided Dice Rolling Simulation

import random #has the random function to randomize!
import time #allow sleeping

while True:
    times = int(input("How many times do you want to roll this dice? "))
    if (times < 0):
        print("Oh, invalid number. Please try again.")
    else:
        break

#Keep track of the tallies of which number was rolled, using dictionaries.
thislist = []
for i in range(0, 7,1):
    thislist.append(0) #quickly populate the list with zeros
    #because of how Python counts, "ones" rolled will be in slot(0)

#Actually roll the numbers now...
for i in range(1,times,1): #roll x times
    number = random.randint(1,6)
    print(f"Dice rolled... {number}!")
    time.sleep(1)
    #Keep tallies:
    for a in range(1,6):
        if number == a:
            thislist[a]+=1

#Check the list - delete later
for i in range(1, 7,1):
    print(f"Dice side {i} was rolled... {thislist[i]} times!")








