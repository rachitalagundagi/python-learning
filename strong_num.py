
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
