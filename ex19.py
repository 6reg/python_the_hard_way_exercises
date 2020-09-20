# function block starts with keyword def followed by name of
#function and parenthesis containing to parameters / aragumnents
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # function body  is
    # statements defining the function that include strings with the args
    # injected with placeholders
    print "You have %d cheeses!" % cheese_count
    print "YOU have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# function call with two ints as args
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# variables assigned int values
amount_of_cheese = 10
amount_of_crackers = 50
# function call with vars
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# func called with math passed as args
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
