# # remove duplicate letter in string

# a="aaabbbcccdddeeffffgg"
# lst=[]
# for char in a:
#     if char not in lst:
#         lst.append(char)
# print(lst)    

# #or

# b=a.split()
# y=list(set(b))
# print(y)

# #--------------------------------------------------

# # remove repeated word in a sentence
# strr= "hello how are you hello"
# b=""
# str= strr.split()

# y = list(set(str))
# print(y)

# for i in y:
#     if i not in y:
#         b.append(i)
#         b.append(" ")
# print(b)


# #-----------------------------------------------------

# # factorial of a number

# x = int(input("enter a number"))
# fact = 1
# for i in range(1,x+1):
#     fact=fact*i
# print(fact)

# #--------------------------------------------------

# # strong number: sum of factorial of each digit = number itself

# x = int(input("enter a number"))
# s= 0
# temp = x
# while(x>0):
#     digit = temp % 10
#     fact=1
#     for i in range(1, digit+1):
#         fact= fact*i
#     s += fact
#     temp= temp//10

# if s==x:
#     print("strong")
# else:
#     print("not strong")        

#--------------------------------------------------------

# ARMSTRONG NUMBER 
'''A positive integer is called an Armstrong number of order n if

abcd... = an + bn + cn + dn + ...
In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

22= 2*2 + 2*2 , 22!= 8 so 22 is not armstrong number 
'''

# x = int(input("enter a number"))
# y = len(str(x))

# temp = x
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**y
#     temp=temp//10

# if sum==x:
#     print("armstrong")
# else:
#     print("not armstrong")        






# a = int(input("enter  a number: "))

# b = len(str(a))
# s=0
# temp =a 
# while(temp>0):
#     digit= temp%10
#     c= digit**b
#     s+=c
#     temp//=10
# if a == s:
#     print("a")
# else:
#     print("na")    

#----------------------------------------------------------------

# STRONG NUMBER 
'''i/p no = sum of factorial of individual digits'''

x= int(input("please enter a number: "))

temp = x
sum= 0

while (temp>0):
    digit=temp%10
    fact=1
    for i in range(1,digit):
        fact*=i+1
    sum+=fact
    print(sum)
    temp//=10
if sum==x:
    print("strong")
else:
    print("not strong")        











