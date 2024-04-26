# '''
# using dictionary following  are the marks scored by respective students: using dictionary convert their marks into grade
# and print that grade with name
# '''
# student_marks={
#     "rachit": 98,
#     'mohit': 99,
#     'sumit': 87,
#     'shreyansh': 79,
#     'murali': 33,
#     'sumit_m': 12
# }

# student_grades={}
# for student in student_marks:
#     marks = student_marks[student]
#     if marks>90:
#         student_grades[student]= "A"
#     elif marks>70:
#         student_grades[student]= "B"
#     elif marks>50:
#         student_grades[student] = "C"
#     elif marks>34:
#         student_grades[student] = "D"
#     else:
#         student_grades[student] = "F"

# print(student_grades)


# '''sort python dictionary by key or value'''
# myDict = {'eravi': 10,
#           'braj': 9,
#           'asanjeev': 15,
#           'dyash': 2,
#           'csuraj': 32}

# myKeys=list(myDict.keys())
# myKeys.sort()
# sorted_dict = {i: myDict[i] for i in myKeys}

# print(sorted_dict)

# #------------------------------------------------------------------------------
# '''python program to find sum of all items in a dictionary
# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

# Input : {‘x’: 25, ‘y’:18, ‘z’:45}
# Output : 88
# '''

# sumDict= {'a': 100, 'b':200, 'c':300}
# sum=0
# for i in sumDict.values():
#     sum+=i
# print(sum)
# #----------------------------------------------------------------

# '''find size of dictionary 
# sys.getsizeof(<dict>) returns memory size of the dictionary object in bytes
# '''
# import sys
# dic1 = {"A": 1, "B": 2}
# dic0 = {}
# dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
# dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

# #printing sizes of the follwoing dictionaries
# print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
# print("Size of dic0: " + str(sys.getsizeof(dic0)) + "bytes")
# print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
# print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")

#--------------------------------------------------------------------------------

'''CODE TO MERGE TWO DICTIONARIES'''

def mergedict(a,b):
    c=(b.update(a))
    return c

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(mergedict(dict1,dict2))


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
