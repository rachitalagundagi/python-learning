# code to convert rachit to rAcHiT

def myfunc(word):
    new_word= ''
    
    for index, letter in enumerate(word):
        if (index+1)%2==0:
            new_word+=letter.upper()
        else:
            new_word+=letter.lower()
    print(new_word)
    return new_word

myfunc("rachit")         
