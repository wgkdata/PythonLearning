namelist = ['A1', 'b13', 'd2', 'A522', 'x09']

startwith = False

for i in namelist:
    if i.lower().startswith('a'):
        print(f'Found! The word is {i};')
        break
else:
    print('Not found')
