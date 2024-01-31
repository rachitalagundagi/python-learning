# Write a method to generate random and unique phone numbers for given number of users.
# Note :
# 1. Phone number size must be minimum 10 digits
# 2. No two users can have the same phone number
#
#
# Sample Input:
# 5
# Sample Output:
# 1231231231
# 1231231232
# 1231231235
# 1231231230
# 1231231239
import random
from random import shuffle


# my_set = [0,1,2,3,4,5,6,7,8,9]

# def shuff():
# shuffle(my_set)
# return my_set

# print(shuff())
# print(shuff())

# a = random.randrange(1000000000, 9999999999)
phoneNumbers = set()
times = int(input("Tell how many numbers you want: "))

for i in range(times):
    a = random.randrange(1000000000, 9999999999)
    phoneNumbers.add(a)

print(phoneNumbers)

# 99999999997

# print(a)