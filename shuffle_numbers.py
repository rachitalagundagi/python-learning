import random
from random import shuffle


my_set = [0,1,2,3,4,5,6,7,8,9]

def shuff():
    shuffle(my_set)
    return my_set

print(shuff())
print(shuff())