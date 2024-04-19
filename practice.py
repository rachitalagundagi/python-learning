# # .format example

# print("My name is {}, my friends name is {}".format("Rachit","Sumukh"))


# # Basic args: Basically pass unlimited arguments

# def myfunc(*args):
#     print(args)
#     print(sum(args))
#     return sum(args) 

# myfunc(20,10,30)

# # args=[20,10,30] print(*args) gives output of 20 10 30 so it basically unpacks the list or set i guess 

#  #example for args and kwargs

# def orderpizza(size, *toppings, **details):
#     print(f"Ordered a {size} pizza with the following toppings:")
    
#     for topping in toppings:
#         print(*topping) #demonstrating *print lol 
#     print("\n Details of the order are:")
#     for key, value in details.items():
#         print(f"{key}: {value}")

# orderpizza("large","cheese","origano","mushroom","chicken", delivery="Home", tip=5)     


# # code for checking if two word input begin with the same alphabet

# def animal_crackers(texts):
#     wordlist = texts.lower().split()
#     if wordlist[0][0]==wordlist[1][0]:#wordlist[firstword][firstletter]==wordlist[secondword][firstletter]
#         print(f"they are same {wordlist}")
#     else:
#         print(f"they are not same {wordlist}")

#     return wordlist

# animal_crackers("red rabbit")
# animal_crackers("blue rabbit")        


# # LAMBDA FUNCTIONS 
# # map function:

# map #syntax 
# def square(num):
#     for i in num:
#         print(i**2)
#     return i**2

# mynums = [1,2,3,4,5]
# square(mynums)
# print(list(mynums))

# #instead of writing function seperately we can use map

# def sq(nums):
#     return nums**2

# mynums=[1,2,3,4,5,6]

# for item in map(sq,mynums):
#     print(item) #for getting result without list

# print(list(map(sq,mynums))) #for getting result in list 

# #filter function: returns a boolean in the same function to filter out stuff
# def check_even(num):
#     return num%2 == 0

# print(list(filter(check_even,mynums)))

# #---------------------
# # lambda expressions
# #-----------------------
# # instead of doing all that just do this 

# sq= lambda num:num**2 # same as def sq(num): return num**2
# print(sq(5)) 

# print("demonstrating lambda function")

# #which can be used in above function of squaring all nums in mynums as follows:

# print(list(map(lambda num:num**2, mynums)))

# print("applying filter of only even nos")

# print(list(filter(lambda num:num%2==0, mynums)))



# class sample():
#     pass 

# my_sample = sample()

# print(type(my_sample))


# #________________________________________

# # class

# class student:
#     def putinfo(self):
#         self.id= int(input("enter student id:"))
#         self.name= input("enter student name:")
#         self.marks=float(input("Enter student marks:"))

#     def display(self):
#         print("student id:",self.id)
#         print("student name:",self.name)
#         print("student marks:",self.marks)

# a= student()
# a.putinfo()
# a.display()

# #---------------------------------------
# class faculty:
#     def __init__(self,a,b,c):
#         self.id=a
#         self.name=b
#         self.salary=c

#     def display(self):
#         print("faculty id:",self.id)
#         print("faculty name:",self.name)
#         print("faculty salary:",self.salary)

# a=faculty(1,varun,10000)
# b=faculty(2,ram,20000)
# c=faculty(3,rachit,30000) # ...
# a.display
# b.display
# c.display

digit=4
sum=0
for i in range(1,digit+1):
    c=i*1
    sum+=c

print(sum)      