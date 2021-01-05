### is-a relationship between fish and salmon ###
### has-a relationship between salmon and gills ###
### is-a === objects and classes related by a class relationship ###
### has-a === objects and classes related only because they... ###
### ... they reference each other

## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## self has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## self has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## self has-a name
        self.name = name


