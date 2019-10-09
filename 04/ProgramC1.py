list = [9, 41, 12, 3, 74, 15]

smallest_so_far = None

for the_num in list:
    if smallest_so_far is None :
        smallest_so_far = the_num
    elif the_num < smallest_so_far :
        smallest_so_far = the_num

print('List:', list)
print('Minimum value:', smallest_so_far)