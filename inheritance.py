# INHERITANCE 

class animal:
    def __init__(self):
        print("animal created")

    def who_am_i(self):
        print("i am animal")

    def eat(self):
        print("i am eating")

myanimal = animal()

myanimal.eat()
myanimal.who_am_i()

# dog class inheriting from animal class
class dog(animal):
    def __init__(self):
        animal.__init__(self)
        print("dog created")

    def who_am_i(self):  # to overwrite method who_am_i()
        print("I am a dog!")        

mydog = dog()
mydog.eat()      # i had not created a function eat() for dog but since i inherited animal into dog so dog got inherited all properties

mydog.who_am_i()
     