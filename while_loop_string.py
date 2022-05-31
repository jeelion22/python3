# prints string from left to right by parsing from it from right to left
# parses reverse
#prints from left to right in newlines
print('string from left to right in a newline by parsing it from right to left')

inp = input('Enter string: ')

index = 0

while index > -len(inp) :
  ind = -index - len(inp)
  x = inp[ind]

  print(x)

  index = index - 1
