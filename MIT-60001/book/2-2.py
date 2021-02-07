# Write a program that examines three variables - x, y, and z - and prints the largest odd number among them.
# If none of them are odd, it should print a message to that effect.

import random

for i in range(25):
    x, y, z = abs(random.randint(1,3)), abs(random.randint(1,3)), abs(random.randint(1,3))
    
    print("\nx = {}\ny = {}\nz = {}".format(x,y,z))

    if x % 2 == 0:
        if y % 2 == 0 and z % 2 == 0: # three even
            print("There are no odd numbers.")
        elif y % 2 != 0 and z % 2 == 0: # one odd: y 
            print("{} is the largest odd number.".format(y))
        elif y % 2 == 0 and z % 2 != 0: # one odd: z
            print("{} is the largest odd number.".format(z))
        elif y == z: # two odd: y = z 
            print("{} and {} are the same odd number.".format(y,z))
        elif y > z: # two odd: y > z
            print("{} is the largest odd number.".format(y))
        elif y < z: # two odd: y < z
            print("{} is the largest odd number.".format(z))
    elif x % 2 != 0:
        if y % 2 == 0 and z % 2 == 0: # one odd: x
            print("{} is the largest odd number.".format(x))    

        elif y % 2 != 0 and z % 2 ==0: # two odd: x and y
            if x == y: # two odd: x = y
                print("{} and {} are the same odd number.".format(x,y))
            elif x > y: # two odd: x > y
                print("{} is the largest odd number.".format(x))
            elif x < y: # two odd: x < y
                print("{} is the largest odd number.".format(y))

        elif y % 2 == 0 and z % 2 !=0: # two odd: x and z
            if x == z: # two odd: x = z
                print("{} and {} are the same odd number".format(x,z))
            elif x > z: # two odd: x > z
                print("{} is the largest odd number.".format(x))
            elif x < z: # two odd: x < z
                print("{} is the largest odd number.".format(z))
        
        elif y % 2 !=0 and z % 2 != 0: # three odd
            if x == y and x == z: # all are equal
                print("All three numbers are {}!".format(x)) # three odd equal: x = y = z
            elif x > y and x > z: # three odd, one high: x > y and z
                print("All three numbers are odd! {} is the largest odd number.".format(x))
            elif z > x and z > y: # three odd, one high: z > x and y
                print("All three numbers are odd! {} is the largest odd number.".format(z))
            elif y > x and y > z: # three odd, one high: y > x and z
                print("All three numbers are odd! {} is the largest odd number.".format(y))
            elif x > y and x == z: # three odd, two high: (x = z) > y
                print("All three numbers are odd! {} is the largest odd number.".format(x))
            elif x > z and x == y: # three odd, two high: (x = y) > z
                print("All three numbers are odd! {} is the largest odd number.".format(x))
            elif y > x and y == z: # three odd, two high: (y = z) > x
                print("All three numbers are odd! {} is the largest odd number.".format(y))