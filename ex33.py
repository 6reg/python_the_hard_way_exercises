
def countUp(numTimes, b):
    i = 0
    numbers = []
    while i < numTimes:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b 
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    print("The Numbers: ")
    print(numbers)
countUp(6, 2)
