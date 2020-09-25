from sys import argv

script, user_name, age = argv
prompt = '>>'

print "%s you are %s years old." % (user_name, age)

print "Hello %s, this is the %s script." % (user_name, script)
print "Who's your favorite producer %s?" % user_name
producer = raw_input(prompt)

print "Who's your favorite rapper, %s?" % user_name
rapper = raw_input(prompt)

print """
Here are songs that feature both %r and %r.
""" % (producer, rapper)
