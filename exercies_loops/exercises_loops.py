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



def factorial(x): 
    result = 1
    for x in range(1, x + 1):
        result *= x
    return result

print(factorial(1))
print(factorial(8))



