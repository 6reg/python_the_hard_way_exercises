
def countUp(numTimes, b):
    i = 0
    numbers = []
    while i < numtimes:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b 
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    print("The Numbers: ")

countUp(6, 2)
