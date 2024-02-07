
# from distutils.cygwinccompiler import check_config_h
import random
from random import shuffle

globalList = ['','O','']
class ThreeCupGame:
    def shuffleList(list):
        shuffle(list)
        return list
    
    def playerGuess():
        guess = ''
        while guess not in ['0','1','2']:
            guess = input("Guess between 0,1, or 2: ")
        return int(guess)

    def checkGuess(guess):
        myList = ThreeCupGame.shuffleList(globalList)
        while myList[guess] != 'O':
            print(myList)
            guess = int(input("Try Again: "))
            
        return True

if ThreeCupGame.checkGuess(ThreeCupGame.playerGuess()):
    print ("Congratulations")

# userGuess = ThreeCupGame.playerGuess()
# if ThreeCupGame.checkGuess(userGuess):
#     print("Congratulations")






# guess = threeCupGame().player_guess()

#     #CHECK GUESS 
#     check_guess(mixeduplist,guess)





# def threeCupGame():
# #shuffle a list 
    
#     my_list = ['','O','']

#     def shuffle_list(my_list):
#         shuffle(my_list)
#         return my_list

#     #print(shuffle_list())

#     #taking player guess 


#     def player_guess():
#         guess = ''

#         while guess not in ['0','1','2']:
#             guess = input("Guess between 0,1, or 2")

#         return int(guess)      #specifying int because input always returns a string      
      
#     # print(player_guess())

#     # my_index = player_guess()
#     # print(my_index)




#     #check guess 

#     def check_guess(my_list,guess):
#         if my_list[guess] == 'O':
#             print("correct")
#         else:
#             print("wrong guess")
#             print(my_list)
#             threeCupGame()


#     # print(check_guess(shuffle_list(),player_guess()))     





#     #combining all the functions   \\\
#     # INITIAL LIST
#     my_list = ['','O','']

#     # SHUFFLE LIST
#     mixeduplist = threeCupGame().shuffle_list(my_list)        

#     #USER GUESS
#     guess = threeCupGame().player_guess()

#     #CHECK GUESS 
#     check_guess(mixeduplist,guess)

                    
