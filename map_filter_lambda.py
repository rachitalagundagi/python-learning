# LAMBDA FUNCTIONS 
# map function:

map #syntax 
def square(num):
    for i in num:
        print(i**2)
    return i**2

mynums = [1,2,3,4,5]
square(mynums)
print(list(mynums))

#instead of writing function seperately we can use map

def sq(nums):
    return nums**2

mynums=[1,2,3,4,5,6]

for item in map(sq,mynums):
    print(item) #for getting result without list

print(list(map(sq,mynums))) #for getting result in list 

#filter function: returns a boolean in the same function to filter out stuff
def check_even(num):
    return num%2 == 0

print(list(filter(check_even,mynums)))

#---------------------
# lambda expressions
#-----------------------
# instead of doing all that just do this 

sq= lambda num:num**2 # same as def sq(num): return num**2
print(sq(5)) 

print("demonstrating lambda function")

#which can be used in above function of squaring all nums in mynums as follows:

print(list(map(lambda num:num**2, mynums)))

print("applying filter of only even nos")

print(list(filter(lambda num:num%2==0, mynums)))


print(list(map(lambda num:num*2, mynums)))

print(list(filter(lambda num:num<8, mynums)))
