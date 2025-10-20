class Solution(object):

    operations = ["++X","++X","X++"]
    x = 0

    for string in operations:
        if string == 'X++' or string == '++x':
            x += 1 
        if string == 'X--' or string == '--X':
            x -= 1

    print(f'{x}')
    
