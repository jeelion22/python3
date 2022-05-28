print('\nCOMPUTATION FOR COUNTING, SUMMING, AND AVERAGE \n\t\t NUMBERS')
name = input('\tWhat is your name? ')
print('\n\t\tWelcome!', name)

print('\nTo finsh the computation, enter \'done\'\n')
l1 = list()

count = 0
total = 0

while True :
    inp = input('Enter number: ')
    if inp == 'done' :
        break
    try :
        l1.append(float(inp))

    except:
        print('Invalid input')

for i in l1 :
    total = total + i
    count = count + 1

if count > 0 :
    avg = total / count

else :
    avg = 'not available'
print('\n')
#print('List: ', l1)

print('Count', '=', count)
print('Total', '=', total)
print('Average', '=', avg)
print('\n')
