#working with lists as per video no. 11

#strings are a bunch of xters held together by a data type
from typing import List, Tuple

my_list=[1,2,3]
print(my_list)
print(my_list*2)

#adding item into lists

my_list=[1,2,3,4,5]
my_list.append(6)
print(my_list)

my_list.append([7,8])
print(my_list)
my_list=[1,2,3]
my_list.extend([4,5,6])
print(my_list)

list_in_list = (1,2,3,[4,5,6])
print(list_in_list.remove([4,5,6]))
print(list_in_list.remove([4]))