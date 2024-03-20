# class

class student:
    def putinfo(self):
        self.id= int(input("enter student id:"))
        self.name= input("enter student name:")
        self.marks=float(input("Enter student marks:"))

    def display(self):
        print("student id:",self.id)
        print("student name:",self.name)
        print("student marks:",self.marks)

a= student()
a.putinfo()
a.display()

#-----------------------------------------------------------
# __init__
class faculty:
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.salary=c

    def display(self):
        print("faculty id:",self.id)
        print("faculty name:",self.name)
        print("faculty salary:",self.salary)

a=faculty(1,"varun",10000)
b=faculty(2,"ram",20000)
c=faculty(3,"rachit",30000)
a.display()
b.display()
c.display()

# -------------------------------------------------
#UDEMY dog example :

class dog:
    def __init__(self, breed, name, spots):
        # attributes 
        self.breed = breed
        self.name = name
        self.spots = spots #expect boolean true or false 


mydog = dog("golderretreiver", "seethu", False)
print(mydog.breed,mydog.name) 
print(mydog.spots)

# CLASS OBJECT ATTRIBUTE 
class dogg:

    specie = "mammal" # class object attribute

    def __init__(self,breed,name,spots):
        self.breed= breed 
        self.name= name
        self.spots = spots

mydogg = dogg("pug","vodafone","a little i guess, idk")
print(mydogg.specie)    


#METHODS 
class dogg:

    specie = "mammal" # class object attribute

    def __init__(self,breed,name,spots):
        self.breed= breed 
        self.name= name

    def bark(self):
        print("WOOF!!! My name is {} and Im a {}".format(self.name,self.breed))
mydoggo = dogg("german-shephard","ram","yes")
dogg.bark(mydoggo)



#---------------------------------------------------------------------------------

# getting circumference of a cirle 

class circle:

    pi= 3.14

    def __init__(self,radius=1):
        self.radius=radius 
        #an attribute doesnt have to be defined like below
        self.area = radius*radius*circle.pi #or self.pi

    def get_circumference(self):
        a= print(self.radius * self.pi * 2)
        return a
        
mycircle = circle(22)  #changing the value of radius here can do like this also 

print(mycircle.radius,mycircle.pi)
print(mycircle.area)

circle.get_circumference(mycircle)

