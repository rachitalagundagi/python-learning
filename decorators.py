# DECORATORS
'''Allows you to tack on extra functionalty to an already existing function

they use @ operator and are then placed on top of the original function'''

def hello(name):
    print("the hello() function has been executed.")

    def greet():
        print("This is greet() function inside hello() function")

    def welcome():
        print("This is welcome() function inside hello() function")

    if name== 'Ram':
        return greet
    else:
        return welcome


hiiii = hello(name="Ram")
heyyy = hello(name='Tom')

# hiiii()
# heyyy()

hiiii