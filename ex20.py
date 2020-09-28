# import argv from sys
from sys import argv

# get arguments
script, input_file = argv

# define print_all function, which takes one arg (f)
def print_all(f):
    # print the contents of f
    print f.read()

# define rewind function, which takes one arg (f)
def rewind(f):
    # move the file pointer back to the beginning of the file f
    f.seek(0)

# define the print_a_line function, which takes 2 args (line_count, f)
def print_a_line(line_count, f):
    # print line_count, then a line from file f
    print line_count, f.readline()

# set current_file variable to a file pointer to input_file
current_file = open(input_file)

# print string
print "First let's print the whole file:\n"

# call print_all function with current_file as an arg
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
