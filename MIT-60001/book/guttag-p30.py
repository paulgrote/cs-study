# Let s be a string that contains a sequence of decimal numbers separated by commas,
# e.g., s = '1.23,2.4,3.123'. Write a program the prints the sum of the numbers in s.

s = '1.23,2.4,3.123'
num = ''
total = 0.0

for char in s:
    
    if char != ',':
        num = num + char
        print(num)

    elif char == ',':
        total = total + float(num)
        print('TOTAL:' + str(total))
        num = ''

total = total + float(num)
print(total)