# import modules_list 
# print(modules_list.a)

# print(modules_list.area_of_square(3))
# print(modules_list.area_of_circle(3))

#--------------------------------------------------------------------------------------------


# MODULES CAN BE IMPORTED AS SOME SMALL NAME SO YOU DONT HAVE TO TYPE BIG NAME EVERY TIME 
# import nmodules_list as m 
# print(m.a)

# print(m.area_of_square(3))

#---------------------------------------------------------------------------------------------


# TO IMPORT JUST A SPECIFIC FUNCTION
from modules_list import area_of_circle as c

print(c(3))


