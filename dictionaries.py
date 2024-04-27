# DICTIONARIES

phone_nos = {'rachit': 8888,
             'mohit': 6969,
             'shreyansh' : 9999,
             'rachit': 6960,
             'sumit': 'not found',
             'rohit': [3345,55456,4444],
             'manisha':[1111]
}
print(phone_nos)
# no duplicates allowed in keys but allowed in values
# values are mutable

print(len(phone_nos))

'''can also be written as nested values as'''
phone_nos['rachit'] = {'rachit home':1234, 'rachit work':5678}

print(phone_nos['rachit'])
print(phone_nos['rachit']['rachit work'])
print(phone_nos.get('rachit'))


roll_no= {1:"rachit", 2:"mohit", 3:"shreyansh"}
print(roll_no[2]) # to print using key
print(roll_no[2][4])# to print letter

# to change value of a key
phone_nos['mohit'] = 2233
print(phone_nos)


#values can be of any data type but keys are be immutable

# adding new key and value pair
phone_nos['ram']={11111,222222}

print(phone_nos)

del phone_nos["ram"]
print(phone_nos)

phone_nos.pop('shreyansh')
print(phone_nos)

print("popping",phone_nos.popitem())
print(phone_nos)

print(phone_nos.keys()) # to print only keys, similarly to print values .values()

print(len(phone_nos))


# TO MERGE TWO DICTIONARIES 
'''CODE TO MERGE TWO DICTIONARIES'''
#.update() method

def mergedict(a,b):
    b.update(a)
    return b

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(mergedict(dict1,dict2))

# USING KWARGS
def merged(a,b):
    merged_dict={**a,**b}
    return merged_dict

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(merged(dict1,dict2))

marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}

marks.update(internal_marks)


print(marks)


# to DELETE EVERYTHING
print(phone_nos.clear()) #to delete everything


