# create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
<<<<<<< HEAD
        'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}
=======
        'Michigan': 'MI',
        }

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Fancisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville',
        }
>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
<<<<<<< HEAD
=======

>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

<<<<<<< HEAD
=======
# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b
# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
<<<<<<< HEAD
for abbrev, city in list(cities.items()):
=======
for  abbrev, city in list(cities.items()):
>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
