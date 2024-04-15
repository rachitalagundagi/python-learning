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

#--------------------------------------------------

# strong number: sum of factorial of each digit = number itself

x = int(input("enter a number"))
s= 0

while(x>0):
    digit = x % 10
    fact=1
    for i in range(1, digit+1):
        fact= fact*i
    s += fact
    x= x//10

if s==x:
    print("strong")
else:
    print("not strong")        

#--------------------------------------------------------