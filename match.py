#Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

def even_odd(type):
    if type % 2 == 0:
        print('even')
    else: 
        print('odd')

even_odd(int(3))
    