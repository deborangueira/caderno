class Solution(object):

    operations = ["++X","++X","X++"]
    x = 0

    for string in operations:
        if string[1] == "+":
            x += 1
        else:
            x -=1

    print(f'{x}')
    
