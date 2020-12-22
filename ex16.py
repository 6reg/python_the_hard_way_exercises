from sys import argv

script, filename = argv

print(f"We're goint to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("IF yes, RETRURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2= input("line 2: ")

print("I'm goint to write the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

print("and finally, we close it.")
target.close()

