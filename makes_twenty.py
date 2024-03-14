# Gicen 2 intergers, return true if the sum of the integers is 20 or if one of the integer is 20. If not return False 

#   makes_twenty(20,10)--> True
#   makes_twenty(12,8)--> True
#   makes_twenty(2,3)--> False 

def makes_twenty(n1,n2):
    if n1== 20 or n2 == 20:
        print("makes twenty")
    elif n1+n2==20:
        print("makes twenty")
    else:
        print("doesnt make twenty")

makes_twenty(2,3)  
makes_twenty(20,4)              
makes_twenty(6,14)

#or can be written in one line as 
# return if n1==20 or n2==20 or n1+n2==20 

