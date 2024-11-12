# #How old are you? 27
# 
# current_age = input('How old are you? ')
# 
# for 
# print(f'You are {current_age} years old.')
# print(f'In 10 years, you will be {int(current_age) + 10} years old')
# print(f'In 20 years, you will be {int(current_age) + 20} years old')
# print(f'In 30 years, you will be {int(current_age) + 30} years old')
# print(f'In 40 years you will be {int(current_age) + 40} years old')

current_age = int(input('How old are you? '))
print(f'You are {current_age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In {future} years, you will be {current_age + future} years old.')