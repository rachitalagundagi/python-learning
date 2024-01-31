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
# a = random.randrange(1000000000, 9999999999)
phoneNumbers = set()
times = int(input("Tell how many numbers you want: "))

for i in range(times):
    a = random.randrange(1000000000, 9999999999)
    phoneNumbers.add(a)

print(phoneNumbers)

#---------------------------------------------------------------------------------
#Generate n nos of phone numbers with names using dictionaries

import random 
my_dict = {}

phoneNumbers = set()
times = int(input("kitne chaiye? "))
name = []

for i in range(times):
    a = random.randrange(1000000000, 9999999999)
    name=input("hesar heli: ")
    my_dict[name]=a

    
print(my_dict)    


