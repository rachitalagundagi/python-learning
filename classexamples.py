class cylinder:

    pi=3.14 #class object attribute 

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height*self.pi*self.radius**2
    
    def surface_area(self):
        return 2*self.pi*self.radius*self.height + 2*self.pi*self.radius**2
    
c= cylinder(2,3)
print(c.volume())
print(c.surface_area())


# CHALLENGE 

''' create a bank accnt that has two attributes: 
* owner 
* balance

and two methods: 
* deposit
* withdraw 

As an added requirement, withdrawals may not exeed the available balance 

Instantiate your class, make several deposit and withdrawals and test to make sure acnnt cnat be over drawn'''

class account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep=0):
        self.dep = dep 
        self.balance = self.balance+self.dep
        print(f"deposit is {self.dep}, new balance is {self.balance}")

    def withdraw(self,wit=0):
        self.wit = wit
        
        if self.wit<self.balance:
            self.balance = self.balance-self.wit
            print(f"deposit is {self.dep}, new balance is {self.balance}")

        else:
            print("insufficient balance")

#instantiating class
a = account("Rachit",100)

print(a.balance)

print(a.deposit(200))
print(a.withdraw(50))
print(a.balance)


        
                 


