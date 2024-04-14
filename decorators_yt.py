# DECORATORS

#syntax

def decorators(func):
    def wrapper():
        print("transaction started")
    func()
    print("transaciton complete")
    return wrapper

def hello():
    print("hello how are you?")

hello1= decorators(hello)

hello1()
#------------------------------------------------------
# can also be written as :
def decorators(func):
    def wrapper():
        print("transaction started")
    func()
    print("transaciton complete")
    return wrapper

@decorators
def hello():
    print("hello how are you?")

hello()