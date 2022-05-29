count = 0
total = 0

largest = None
smallest =  None

lt = list()

while True :
    inp = input('Enter number: ')
    if inp == 'done' :
        break

    try :
        lt.append(float(inp))

    except :
        print('Invalid input')

for i in lt :
    count = count + 1
    total = total + i

try :
    if len(lt) > 0 :
        avg = total / count
except :
    print('Average is not possible for empty list')

for item in lt :
    if largest is None or item > largest :
        largest = item

    if smallest is None or item < smallest :
        smallest = item

print('Count, Total, Average', count, total, avg)

print('Largest, smallest ', largest, smallest)
