from sys import argv

script, first, second, third = argv

first = raw_input("Add the name of the first variable: ")
print "The script is called:", script
print "Your second variable is:", second
third = raw_input("add the name of your third var here: ")

print "You typed: %r" % first
print "You also typed: %r" % third
