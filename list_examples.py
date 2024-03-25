# LIST CODING EXAMPLES

'''write a code to swap first and last element of a list'''

def swap(list):
    count = len(list)
    temp = list[0]
    list[0]=list[count-1]
    list[count-1]=temp
    print(list)
    return list

a=[1,2,3,4,5,6,7]
print(swap(a))

#____________________________________________________________________________________________________________________________________

'''
Given a list in Python and provided the positions of the elements,
 write a program to swap the two elements in the list. 
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]   '''

def noswap(list):
    pos1= int(input("please enter first no of the list like 1st no or 2nd no... to be swapped like 1,2,3...: "))
    pos2= int(input("enter the second to to be swapped with: "))

    size = len(list)

    temp = list[pos2-1]
    list[pos2-1] = list[pos1-1]
    list[pos1-1]=temp

    print(list)
    return list

a=[1,2,3,4,5,6]
noswap(a)

#=--------------------------------------------------------------------------------------------------

