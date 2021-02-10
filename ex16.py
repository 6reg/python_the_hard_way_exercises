from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If not, hit control c (^C).")
print("Else hit return.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating file.")
target.truncate()

print("Now input three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Writing to file..")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And close it")
target.close()
