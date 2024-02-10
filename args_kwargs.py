# .format example

print("My name is {}, my friends name is {}".format("Rachit","Sumukh"))


# Basic args: Basically pass unlimited arguments

def myfunc(*args):
    print(args)
    print(sum(args))
    return sum(args)

myfunc(20,10,30)

# args=[20,10,30] print(*args) gives output of 20 10 30 so it basically unpacks the list or set i guess 

 #example for args and kwargs

def orderpizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with the following toppings:")
    
    for topping in toppings:
        print(*topping) #demonstrating *print lol 
    print("\n Details of the order are:")
    for key, value in details.items():
        print(f"{key}: {value}")

orderpizza("large","cheese","origano","mushroom","chicken", delivery="Home", tip=5)            