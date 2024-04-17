 # SETS : unordered, immutable, no duplicates, cant use indexing

''' iterate over a set in python'''
gem=("sunny")
for id,val in enumerate(gem, start=1): # enumerate gives nos to each letter 
    print(id,val)

#---------------------------------------------------------------------------------    

# REMOVING ITEMS FROM A SET 
# pop(), discard90, remove(), clear()
my_set={2,3,4,5,6,7}

print(my_set.pop())
print(my_set)
print(my_set.pop)
#---------------------------------------------

# CHECK IF TWO LISTS HAVE SAME ELEMENT
def common_data(list1, list2):
    result = False
 
    for x in list1: 
        for y in list2:
   
            if x == y:
                result = True
                return result 
                 
    return result
     
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))
#---------------------------------------------------------

