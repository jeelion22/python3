print('\nCOMPUTATION FOR COUNTING, SUMMING, AND AVERAGE \n\t\t NUMBERS')
name = input('\tWhat is your name? ')
print('\n\t\tWelcome!', name)

print('\nTo finsh the computation, enter \'done\'\n')
# create an empty list
l1 = list()

# initialize variables

count = 0
total = 0

# loop works for adding numbers in the list

while True :
    inp = input('Enter number: ')
    if inp == 'done' :
        break
    try :
        l1.append(float(inp))

    except:
        print('Invalid input')

# computation begins from here
        
for i in l1 :
    total = total + i
    count = count + 1

if count > 0 : # avoids math error in the way of statistical sense
    avg = total / count

else :
    avg = 'not available'
    
print('\n')

#print('List: ', l1) if you need the list you entered, remove '#'

# prints the result

print('Count', '=', count)
print('Total', '=', total)
print('Average', '=', avg)
print('\n')
