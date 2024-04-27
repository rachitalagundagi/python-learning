''' Given a dictionary with a values list, extract the key whose value has the most unique values.
Input : test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]} 
Output : "Gfg" 
Explanation : "Gfg" having max unique elements i.e 5.'''

def longest(dict):
    flag=0
    for i in dict:
        if len(set(dict[i]))>flag:
            flag=len(set(dict[i]))
            print(i)
        

test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3,3,3,3,1,2,5,99], "Best" : [9, 9, 6, 5, 5]}

longest(test_dict)