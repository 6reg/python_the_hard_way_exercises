from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "What is the script called?"
y = raw_input("Script name ")
print "Ok, you think the script is called %r." % y
print "Your first variable is:", first
print "Your sceond variable is:", second
print "Your third variable is:", third
