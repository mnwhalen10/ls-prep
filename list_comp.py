# squares = [x * x for x in range(5)]
# print(squares)

# multiples_of_6 = [number for number in range(20)
#                     if number % 6 ==0]
# print(multiples_of_6)

# even_squares = [number * number 
#                 for number in range(10)
#                 if number % 2 ==0]
# print(even_squares)

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

#names = [name.upper() for name in cats_colors ]
#print(names)
## ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']
#color = [name.upper() for name in cats_colors.values()]
#print(color)
#total = [f'{key.upper()} : {value.upper()}' for key, value in cats_colors.items#()]
#print(total)
# orange_cat = [name.upper() 
#             for name in cats_colors
#             if cats_colors[name] == 'orange']
# print(orange_cat)
# 
# brown_cat = [name.upper()
#             for name in cats_colors
#             if cats_colors[name] == 'brown']
# print(f'the brown cat is {brown_cat}!')

names_begin_with_L = [name.upper() 
                    for name in cats_colors
                    if cats_colors[name] == 'orange'
                    if name[0] == 'L']
print(names_begin_with_L)



