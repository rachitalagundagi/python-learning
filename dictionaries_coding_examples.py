'''
using dictionary following  are the marks scored by respective students: using dictionary convert their marks into grade
and print that grade with name
'''
student_marks={
    "rachit": 98,
    'mohit': 99,
    'sumit': 87,
    'shreyansh': 79,
    'murali': 33,
    'sumit_m': 12
}

student_grades={}
for student in student_marks:
    marks = student_marks[student]
    if marks>90:
        student_grades[student]= "A"
    elif marks>70:
        student_grades[student]= "B"
    elif marks>50:
        student_grades[student] = "C"
    elif marks>34:
        student_grades[student] = "D"
    else:
        student_grades[student] = "F"

print(student_grades)


'''sort python dictionary by key or value'''
myDict = {'eravi': 10,
          'braj': 9,
          'asanjeev': 15,
          'dyash': 2,
          'csuraj': 32}

myKeys=list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)

#------------------------------------------------------------------------------
'''python program to find sum of all items in a dictionary
Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600

Input : {‘x’: 25, ‘y’:18, ‘z’:45}
Output : 88
'''

sumDict= {'a': 100, 'b':200, 'c':300}
sum=0
for i in sumDict.values():
    sum+=i
print(sum)
#----------------------------------------------------------------

'''find size of dictionary 
sys.getsizeof(<dict>) returns memory size of the dictionary object in bytes
'''
import sys
dic1 = {"A": 1, "B": 2}
dic0 = {}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

#printing sizes of the follwoing dictionaries
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic0: " + str(sys.getsizeof(dic0)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")