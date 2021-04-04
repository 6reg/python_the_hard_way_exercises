import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listOfHeadsOrTails = []
    flip = random.randint(0, 1) 
    for i in range(100):
        if flip == 0:
         listOfHeadsOrTails += "H"
        else:
         listOfHeadsOrTails += "T"

    # Code that checks if there is a streak of 6 heads or tails in a row. 
    for i in range(len(listOfHeadsOrTails)):
        if i == 0:
            pass
        elif listOfHeadsOrTails[i] == listOfHeadsOrTails[i - 1]:
            streak += 1
        else:
            streak = 0
        
        if streak == 6:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
