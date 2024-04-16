# ARMSTRONG NUMBER 
'''A positive integer is called an Armstrong number of order n if

abcd... = an + bn + cn + dn + ...
In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

22= 2*2 + 2*2 , 22!= 8 so 22 is not armstrong number 
'''

x = int(input("enter a number"))
y = len(str(x))

temp = x
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**y
    temp//=10

if sum==x:
    print("armstrong")
else:
    print("not armstrong")  