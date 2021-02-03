### is-a relationship between fish and salmon ###
### has-a relationship between salmon and gills ###
### is-a === objects and classes related by a class relationship ###
### has-a === objects and classes related only because they... ###
### ... they reference each other

# Animal is-a object
class Animal(object):
    print("Animal is-a object")

Animal()
# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # self has-a name
        self.name = name
        print(self, name) 

# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # self has-a name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        # self has-a name
        self.name = name
        # Person has-a pet
        self.pet = None

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee is-a self, self has-a name
        super(Employee, self).__init__(name)
        # self has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-a pet, pet is-a rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a Salmon()
crouse = Salmon()

# harry is-a halibut
harry = Halibut()
