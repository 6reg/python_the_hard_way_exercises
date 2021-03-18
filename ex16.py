from sys import argv

script, filename = argv

<<<<<<< HEAD
print(f"We're goint to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("IF yes, RETRURN.")
=======
print(f"We're going to erase {filename}.")
print("If not, hit control c (^C).")
print("Else hit return.")
>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b

input("?")

print("Opening the file...")
target = open(filename, 'w')

<<<<<<< HEAD
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2= input("line 2: ")

print("I'm goint to write the file.")
=======
print("Truncating file.")
target.truncate()

print("Now input three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Writing to file..")
>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
<<<<<<< HEAD

print("and finally, we close it.")
target.close()

=======
target.write(line3)
target.write("\n")

print("And close it")
target.close()
>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b
