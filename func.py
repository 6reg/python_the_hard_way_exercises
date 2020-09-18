def grocery(meat, produce):
    print "I need to buy %r and %r." % (meat, produce)
    return meat + produce

meat = raw_input("What do you need to buy? ")


grocery("steak", "apples")

grocery(10, 15)

meat = "steak"
produce = "apples"
grocery(meat, produce)

grocery(19 * 2, 14 * 2)
