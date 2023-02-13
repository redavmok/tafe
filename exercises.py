# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using 
# try and except and print an error message and skip to the next number.


def new_func():
    while True:
        try:
            line = input('> ')
            if line == 'done':
                break
            elif line / 1 == False:
                print('Error!')
                continue
            print(line)
        except:
            #print('Error!')
            continue

    print(line)
new_func()
print('Done!')

sum = 0
total = 0.0
while True: 
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        input2 = int(line)
    except:
        print('Invalid input')
        continue
        #print(input2)
    total = total + input2
    sum = sum + 1
    
print('Done!')
print(total, sum, total/sum)

maximum = None
minimum = None
while True: 
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        input2 = int(line)
    except:
        print('Invalid input')
        continue
        #print(input2)
    if input2 is None or input2 > maximum:
            maximum = input2
    elif input2 is None or input2 < minimum:
            minimum = input2
    continue
    
print('Done!')
print(maximum, minimum)

# largest = None
# print('Before:', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest :
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)