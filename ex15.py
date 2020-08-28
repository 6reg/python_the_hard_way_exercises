# from module "sys", import func or parameter "argv" argv= script name then parameters typed into cmd
from sys import argv

# accepts two arguments = script and filename
script, filename = argv

# opens file
txt = open(filename)

print "Here's your file %r:" % filename

# txt gets read command with no parameters, which prints out contents of txt
print txt.read()

# take user input to define file_again var then command open with paramter file_a
#print "Type the filename again:"
#file_again = raw_input("> ")

#txt_again = open(file_again)

#print txt_again.read()
