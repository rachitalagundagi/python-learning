# LISTS EVERYTHING TO KNOW

numbers = [10,0,-1,7,8,10,-67,0]

# finding out lenght of list
print(len(numbers))

# printing numbers in range using index
print(numbers[0:2])

print(numbers[0:])

print(numbers[:6])

print(numbers[0::2]) #print every 0::nth number or element

print(max(numbers))

#numbers = [10,0,-1,7,8,10,-67,0]

#add one element at end of list
numbers.append(666)
print(numbers)


#add multiple elements to list
numbers.extend([33,44,55])
print(numbers)

print(numbers[1:4]) #print range 

#remove elements from list
print("element removed is: ",numbers.pop(5))
print(numbers)

print(numbers.count(0)) #count how many times number is repeated 

# REMOVE MULTIPLE ELEMENTS FROM LIST
del numbers[1:3]
print(numbers)

#for removing with conditons can do using list_name.remove() function
list1 = [0,2,3,4,5,6,7,8]
for num in list1:
    if num%2==0:
        list1.remove(num)
print(list1)        























# # LIST CODING EXAMPLES

# '''write a code to swap first and last element of a list'''

# def swap(list):
#     count = len(list)
#     temp = list[0]
#     list[0]=list[count-1]
#     list[count-1]=temp
#     print(list)
#     return list

# a=[1,2,3,4,5,6,7]
# print(swap(a))

# #____________________________________________________________________________________________________________________________________

# '''
# Given a list in Python and provided the positions of the elements,
#  write a program to swap the two elements in the list. 
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]   '''

# def noswap(list):
#     pos1= int(input("please enter first no of the list like 1st no or 2nd no... to be swapped like 1,2,3...: "))
#     pos2= int(input("enter the second to to be swapped with: "))

#     size = len(list)

#     temp = list[pos2-1]
#     list[pos2-1] = list[pos1-1]
#     list[pos1-1]=temp

#     print(list)
#     return list

# a=[1,2,3,4,5,6]
# noswap(a)

# #--------------------------------------------------------------------------------------------------
# '''Check if element exists in list in Python
# Input: test_list = [1, 6, 3, 5, 3, 4]
#    3:  Check if 3 exist or not.
# Output: True
# Explanation: The output is True because the element we are looking is exist in the list.'''

# def check(numm):
#     count = 0
#     a = [1,6,3,5,3,4]
#     if numm in a:
#         b=a.count(numm)
#         print(f"number {numm} present {b} times")
#     else: print(f"number {numm} not present in {a}")    

# check(3)     
# check(88)       
# #-------------------------------------------------------------------------------------------------------
# '''reversing a list'''
# a=[1,2,3,4,5,6]
# print(a[::-1])

# print(list(reversed(a)))
# #----------------------------------------------------------------------------------------------

