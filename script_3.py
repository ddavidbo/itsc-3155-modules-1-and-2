inp = input('Enter a string: ')

temp = {}
for x in inp.lower():
    if x in temp:
        temp[x] += 1
    else:
        temp[x] = 1
print(temp)