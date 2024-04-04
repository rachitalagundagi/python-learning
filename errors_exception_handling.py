# # THREE IMPORTANT KEYWORDS :

# '''try:block of code to be attempted
#  except:block of code will execute in case there is error in try block 
#    finally;  Final block of code to be exercuted regaredless of an error'''

# # try:
# #     #want to attempt this code, may have an error 
# #     result = 10+10 

# # except:
# #     print("there was an error in adding")

# # print(result)    

# #----------------------------------------------------------------------------
# # TRY EXCEPT ELSE METHOD 
# try:
#     #want to attempt this code, may have an error 
#     result = 10+10 

# except:
#     print("there was an error in adding")
# else: print("add went well!")
# print(result)  

#--------------------------------------------------------------------------------

# YOUTUBE LECTURE

a = input("Please enter the no whose multiplication table you want.")
print(f"multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}" )        

except:
    print("Invalid input") #basically doesnt stop running the code if one error occurs 

print("end of code") 

#-------------------------------------------------------------------------------------------

# there are various errors in python like IndexError, ValueError etc

#-------------------------------------------------------------------------------------------

# ERRORS AND EXCEPTION HANDLING

try:
    #code you wanna attempt
except:
    # print msg when error occurs
   
finally:
    #block of code that runs at the end no matter what

#-----------------------------------------------------------

# code to demonstrate errors and exception handling in a function

def ask_for_int():
    try:
        result = int(input("please provide number: "))

    except:
        print("oops!! not a number")
    finally:
        print("end of program")

ask_for_int()


#------------------------------------------------------------------
# DO WHILE LOOP WITH CONTINUE
i=0
while True:
    print(i)
    i+=1
    if(i%100==0):
        break

i=0
while True:
    for i in range(12):
       
        if(i==10):
            continue
            print(i)

# list of coding examples for future reference link:
#  https://www.w3resource.com/python-exercises/python-exception-handling-exercises.php


#---------------------------------------------------------------

# asking for int with while true

def askforint():
    while True:
            try:
                result = int(input("provide a no: "))
            except:
                print("entered value is not an integer")
                continue
            else:
                print("thank you")
                break
            finally:
                print("you can ty again if you wish")

#---------------------------------------------------------------
#udemy hw

# 1.
'''
for i in['a','b','c']:
    print(i**2)
TYPE ERROR
'''

try:
    for i in['a','b','c']:
        print(i**2)

except TypeError: #no need to mention the type of error to catch all typrs of issues
    print("theres a type error")
#-------------------------------------------------------------

#2.
'''
Handle the exception thrown by the code below by using try and except blocks. then finally use block to print "all done"
x=5
y=0
z=x/y
'''
#ZERO DIVISION ERROR
try:
    x=5
    y=0
    z=x/y
   
except:
    print("cant divde by 0 as it causes zero divison error")

finally:
    print("all done")

#-------------------------------------------------------------

# 3.
'''
write a funciton that asks for an integer and prints the square of it. use a while loop eitha a try , except, else block to account for incorrect inputs.
'''

def ask():
    while True:
        try:
            result=int(input("please enter an integer that needs to be squared")
            print(result**2)
        except:
            print("wrong input please try again")
            continue
        else:
            print("thankyou!")
            break
