import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listOfHeadsOrTails = []
    flip = random.randint(0, 1) 
    if flip == 0:
        listOfHeadsOrTails += "H"
    else:
        listOfHeadsOrTails += "T"

    if listOfHeadsOrTails[n] == listOfHeadsOrTails[n+1]
    # Code that checks if there is a streak of 6 heads or tails in a row. 
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
