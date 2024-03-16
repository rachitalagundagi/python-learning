# Write a function that capitalizes the first and fourth letters of a name 
#   macdonald--> MacDonald

#can do as firstletter= word[0]
#next=word[1:3]
#fourtletter=word[4]
#rest=word[5:]
#new_word = firstletter.upper() + next + fourthletter.upper() + rest

#   OR USE CAPITALIZE()

def capitalizer(word):
    new_word=''
    first_half= word[:3]
    second_half= word[3:]
    new_word=first_half.capitalize()+second_half.capitalize()
    print(new_word)
    return new_word


capitalizer("macdonald")