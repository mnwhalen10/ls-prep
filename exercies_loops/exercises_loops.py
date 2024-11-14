# my_list = [6, 3, 0, 11, 20, 4, 17]
# #counter = 0
# #while counter < len(my_list):
# #    number = my_list[counter]
# #    if number % 2 == 0:
# #        print(number)
# #    counter += 1
# 
# for number in my_list:
#     if number % 2 != 0:
#         print(number)

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]
# 
# for list in my_list:
#     for number in list: 
#         if number % 2 == 0:
#             print(number)

# write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.
# create new list with even and odd strings 

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]
# 
# new_list = []
# 
# for number in my_list:
#     if number % 2 == 0:
#         new_list.append('even')
#     else:
#         new_list.append('odd')
# print(new_list)



# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]

# def find_integers(things):
#     return [ element
#             for element in things
#             if type(element) is int ]
# 
# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# 
# integers = find_integers(my_tuple)
# 
# print(integers)  # [1, 3, -4]

# You can use the expression type(object) is int to determine whether an object is an integer. For instance:

# Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }
# 
# new_string = { string: len(string) 
#             for string in my_set 
#             if len(string) % 2 != 0}
# print(new_string)



# def factorial(x): 
#     result = 1
#     for x in range(1, x + 1):
#         result *= x
#     return result
# 
# print(factorial(1))
# print(factorial(8))

# The following code uses the randrange function from Python's random library to obtain and print a random integer within a given range. Using a while loop, it keeps running until it finds a random number that matches the last number in the range. Refactor the code so it doesn't require two different invocations of randrange.

# import random
# 
# highest = 10
# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break

# my_list = [
#   [1, 3, 6, 11],
#   [4, 2, 4],
#   [9, 17, 16, 0],
# ]
# 
# outer_index = 0
# while outer_index < len(my_list):
#     inner_index = 0
#     while inner_index < len(my_list[outer_index]):
#         number = my_list[outer_index][inner_index]
#         if number % 2 == 0:
#             print(number)
# 
#         inner_index += 1
# 
#     outer_index += 1

import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

# All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])
# 
# # All of these should print True
# 
# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])

# import math 
# print(math.sqrt(36))
# print(math.sqrt(88))
# print(math.pi * math.pi)

# greeting = 'Salutations'
# 
# def well_howdy(who):
#     global greeting
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')
# 
# well_howdy('Angie')
# print(greeting)

# def set_pi():
#     global pi
#     pi = 3.1415
# 
# set_pi()
# print(pi)

# # import math
# 
# print(math.sqrt(37))
# 
# import math as m
# 
# print(m.sqrt(37))
# 
# from math import sqrt
# 
# print(sqrt(37))

# def sum_of_squares(num1, num2):
#     def square (number):
#         return number * number 
#     return square(num1) + square(num2)
# 
# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)

# counter = 0
# 
# def increment_counter():
#     global counter
#     counter += 1
#     
# 
# print(counter)                # 0
# 
# increment_counter()
# print(counter)                # 1
# 
# increment_counter()
# print(counter)                # 2
# 
# counter = 100
# increment_counter()
# print(counter)                # 101

# def all_actions():
#     counter = 0
# 
#     def increment_counter():
#         nonlocal counter
#         counter += 1
# 
#     print(counter)                # 0
# 
#     increment_counter()
#     print(counter)                # 1
# 
#     increment_counter()
#     print(counter)                # 2
# 
#     counter = 100
#     increment_counter()
#     print(counter)                # 101
# 
# all_actions()

