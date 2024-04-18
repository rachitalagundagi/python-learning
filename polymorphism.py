class dog:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return(self.name +" says woof!")    

class cat:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return(self.name+" says meow!")
  


niko= dog("niko")
felix = cat("felix")

print(niko.speak())

for pet_class in [niko,felix]:
    print(type(pet_class))
    print(pet_class.speak())