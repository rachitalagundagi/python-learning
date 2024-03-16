    

#pre requisites 
#    printting reverse statement: 
text ="seethu is a good cat"
newtext= text.split()[::-1]      #convert it into a list using .split() then reverse it using either .sort(reverse=True) or like in the code 
print(newtext)

#solution: 
def joinerboi(sentence):
    newsent=''                                      # new_sentence.sort(reverse=True) 

    newsent =' '.join(sentence.split()[::-1]) #or fo like: new_sentence= sentence[::-1] where in list [from:to] or [exclude: how many elements: skip bw elements]
    print(newsent)
joinerboi("seethu is a good cat")    

